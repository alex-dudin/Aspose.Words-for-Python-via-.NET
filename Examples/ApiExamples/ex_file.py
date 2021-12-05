import unittest
import io
import os
import glob
from datetime import datetime

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExFile(ApiExampleBase):

    def test_catch_file_corrupted_exception(self):

        #ExStart
        #ExFor:FileCorruptedException
        #ExSummary:Shows how to catch a FileCorruptedException.
        try:

            # If we get an "Unreadable content" error message when trying to open a document using Microsoft Word,
            # chances are that we will get an exception thrown when trying to load that document using Aspose.Words.
            doc = aw.Document(MY_DIR + "Corrupted document.docx")

        except Exception as e:

            print(e)

        #ExEnd

    def test_detect_encoding(self):

        #ExStart
        #ExFor:FileFormatInfo.Encoding
        #ExFor:FileFormatUtil
        #ExSummary:Shows how to detect encoding in an html file.
        info = aw.FileFormatUtil.detect_file_format(MY_DIR + "Document.html")

        self.assertEqual(aw.LoadFormat.HTML, info.load_format)

        # The Encoding property is used only when we create a FileFormatInfo object for an html document.
        self.assertEqual("Western European (Windows)", info.encoding)
        #ExEnd

        info = aw.FileFormatUtil.detect_file_format(MY_DIR + "Document.docx")

        self.assertEqual(aw.LoadFormat.DOCX, info.load_format)
        self.assertIsNone(info.encoding)

    def test_file_format_to_string(self):

        #ExStart
        #ExFor:FileFormatUtil.ContentTypeToLoadFormat(String)
        #ExFor:FileFormatUtil.ContentTypeToSaveFormat(String)
        #ExSummary:Shows how to find the corresponding Aspose load/save format from each media type string.
        # The ContentTypeToSaveFormat/ContentTypeToLoadFormat methods only accept official IANA media type names, also known as MIME types.
        # All valid media types are listed here: https://www.iana.org/assignments/media-types/media-types.xhtml.

        # Trying to associate a SaveFormat with a partial media type string will not work.
        with self.assertRaises(Exception):
            aw.FileFormatUtil.content_type_to_save_format("jpeg")

        # If Aspose.Words does not have a corresponding save/load format for a content type, an exception will also be thrown.
        with self.assertRaises(Exception):
            aw.FileFormatUtil.content_type_to_save_format("application/zip")

        # Files of the types listed below can be saved, but not loaded using Aspose.Words.
        with self.assertRaises(Exception):
            aw.FileFormatUtil.content_type_to_load_format("image/jpeg")

        self.assertEqual(aw.SaveFormat.JPEG, aw.FileFormatUtil.content_type_to_save_format("image/jpeg"))
        self.assertEqual(aw.SaveFormat.PNG, aw.FileFormatUtil.content_type_to_save_format("image/png"))
        self.assertEqual(aw.SaveFormat.TIFF, aw.FileFormatUtil.content_type_to_save_format("image/tiff"))
        self.assertEqual(aw.SaveFormat.GIF, aw.FileFormatUtil.content_type_to_save_format("image/gif"))
        self.assertEqual(aw.SaveFormat.EMF, aw.FileFormatUtil.content_type_to_save_format("image/x-emf"))
        self.assertEqual(aw.SaveFormat.XPS, aw.FileFormatUtil.content_type_to_save_format("application/vnd.ms-xpsdocument"))
        self.assertEqual(aw.SaveFormat.PDF, aw.FileFormatUtil.content_type_to_save_format("application/pdf"))
        self.assertEqual(aw.SaveFormat.SVG, aw.FileFormatUtil.content_type_to_save_format("image/svg+xml"))
        self.assertEqual(aw.SaveFormat.EPUB, aw.FileFormatUtil.content_type_to_save_format("application/epub+zip"))

        # For file types that can be saved and loaded, we can match a media type to both a load format and a save format.
        self.assertEqual(aw.LoadFormat.DOC, aw.FileFormatUtil.content_type_to_load_format("application/msword"))
        self.assertEqual(aw.SaveFormat.DOC, aw.FileFormatUtil.content_type_to_save_format("application/msword"))

        self.assertEqual(aw.LoadFormat.DOCX,
            aw.FileFormatUtil.content_type_to_load_format(
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"))
        self.assertEqual(aw.SaveFormat.DOCX,
            aw.FileFormatUtil.content_type_to_save_format(
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"))

        self.assertEqual(aw.LoadFormat.TEXT, aw.FileFormatUtil.content_type_to_load_format("text/plain"))
        self.assertEqual(aw.SaveFormat.TEXT, aw.FileFormatUtil.content_type_to_save_format("text/plain"))

        self.assertEqual(aw.LoadFormat.RTF, aw.FileFormatUtil.content_type_to_load_format("application/rtf"))
        self.assertEqual(aw.SaveFormat.RTF, aw.FileFormatUtil.content_type_to_save_format("application/rtf"))

        self.assertEqual(aw.LoadFormat.HTML, aw.FileFormatUtil.content_type_to_load_format("text/html"))
        self.assertEqual(aw.SaveFormat.HTML, aw.FileFormatUtil.content_type_to_save_format("text/html"))

        self.assertEqual(aw.LoadFormat.MHTML, aw.FileFormatUtil.content_type_to_load_format("multipart/related"))
        self.assertEqual(aw.SaveFormat.MHTML, aw.FileFormatUtil.content_type_to_save_format("multipart/related"))
        #ExEnd

    def test_detect_document_encryption(self):

        #ExStart
        #ExFor:FileFormatUtil.DetectFileFormat(String)
        #ExFor:FileFormatInfo
        #ExFor:FileFormatInfo.LoadFormat
        #ExFor:FileFormatInfo.IsEncrypted
        #ExSummary:Shows how to use the aw.FileFormatUtil class to detect the document format and encryption.
        doc = aw.Document()

        # Configure a SaveOptions object to encrypt the document
        # with a password when we save it, and then save the document.
        save_options = aw.saving.OdtSaveOptions(aw.SaveFormat.ODT)
        save_options.password = "MyPassword"

        doc.save(ARTIFACTS_DIR + "File.detect_document_encryption.odt", save_options)

        # Verify the file type of our document, and its encryption status.
        info = aw.FileFormatUtil.detect_file_format(ARTIFACTS_DIR + "File.detect_document_encryption.odt")

        self.assertEqual(".odt", aw.FileFormatUtil.load_format_to_extension(info.load_format))
        self.assertTrue(info.is_encrypted)
        #ExEnd

    def test_detect_digital_signatures(self):

        #ExStart
        #ExFor:FileFormatUtil.DetectFileFormat(String)
        #ExFor:FileFormatInfo
        #ExFor:FileFormatInfo.LoadFormat
        #ExFor:FileFormatInfo.HasDigitalSignature
        #ExSummary:Shows how to use the aw.FileFormatUtil class to detect the document format and presence of digital signatures.
        # Use a FileFormatInfo instance to verify that a document is not digitally signed.
        info = aw.FileFormatUtil.detect_file_format(MY_DIR + "Document.docx")

        self.assertEqual(".docx", aw.FileFormatUtil.load_format_to_extension(info.load_format))
        self.assertFalse(info.has_digital_signature)

        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.sign_time = datetime.now()

        certificate_holder = aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw", None)
        aw.digitalsignatures.DigitalSignatureUtil.sign(MY_DIR + "Document.docx", ARTIFACTS_DIR + "File.detect_digital_signatures.docx",
            certificate_holder, sign_options)

        # Use a new FileFormatInstance to confirm that it is signed.
        info = aw.FileFormatUtil.detect_file_format(ARTIFACTS_DIR + "File.detect_digital_signatures.docx")

        self.assertTrue(info.has_digital_signature)

        # We can load and access the signatures of a signed document in a collection like this.
        self.assertEqual(1, aw.digitalsignatures.DigitalSignatureUtil.load_signatures(ARTIFACTS_DIR + "File.detect_digital_signatures.docx").count)
        #ExEnd

    def test_save_to_detected_file_format(self):

        #ExStart
        #ExFor:FileFormatUtil.DetectFileFormat(Stream)
        #ExFor:FileFormatUtil.LoadFormatToExtension(LoadFormat)
        #ExFor:FileFormatUtil.ExtensionToSaveFormat(String)
        #ExFor:FileFormatUtil.SaveFormatToExtension(SaveFormat)
        #ExFor:FileFormatUtil.LoadFormatToSaveFormat(LoadFormat)
        #ExFor:Document.OriginalFileName
        #ExFor:FileFormatInfo.LoadFormat
        #ExFor:LoadFormat
        #ExSummary:Shows how to use the aw.FileFormatUtil methods to detect the format of a document.
        # Load a document from a file that is missing a file extension, and then detect its file format.
        with open(MY_DIR + "Word document with missing file extension", "rb") as doc_stream:

            info = aw.FileFormatUtil.detect_file_format(doc_stream)
            load_format = info.load_format

            self.assertEqual(aw.LoadFormat.DOC, load_format)

            # Below are two methods of converting a LoadFormat to its corresponding SaveFormat.
            # 1 -  Get the file extension string for the LoadFormat, then get the corresponding SaveFormat from that string:
            file_extension = aw.FileFormatUtil.load_format_to_extension(load_format)
            save_format = aw.FileFormatUtil.extension_to_save_format(file_extension)

            # 2 -  Convert the LoadFormat directly to its SaveFormat:
            save_format = aw.FileFormatUtil.load_format_to_save_format(load_format)

            # Load a document from the stream, and then save it to the automatically detected file extension.
            doc = aw.Document(doc_stream)

            self.assertEqual(".doc", aw.FileFormatUtil.save_format_to_extension(save_format))

            doc.save(ARTIFACTS_DIR + "File.SaveToDetectedFileFormat" + aw.FileFormatUtil.save_format_to_extension(save_format))

        #ExEnd

    def test_detect_file_format__save_format_to_load_format(self):

        #ExStart
        #ExFor:FileFormatUtil.SaveFormatToLoadFormat(SaveFormat)
        #ExSummary:Shows how to convert a save format to its corresponding load format.
        self.assertEqual(aw.LoadFormat.HTML, aw.FileFormatUtil.save_format_to_load_format(aw.SaveFormat.HTML))

        # Some file types can have documents saved to, but not loaded from using Aspose.Words.
        # If we attempt to convert a save format of such a type to a load format, an exception will be thrown.
        with self.assertRaises(Exception):
            aw.FileFormatUtil.save_format_to_load_format(aw.SaveFormat.JPEG)
        #ExEnd

    def test_extract_images(self):

        #ExStart
        #ExFor:Shape
        #ExFor:Shape.ImageData
        #ExFor:Shape.HasImage
        #ExFor:ImageData
        #ExFor:FileFormatUtil.ImageTypeToExtension(ImageType)
        #ExFor:ImageData.ImageType
        #ExFor:ImageData.Save(String)
        #ExFor:CompositeNode.GetChildNodes(NodeType, bool)
        #ExSummary:Shows how to extract images from a document, and save them to the local file system as individual files.
        doc = aw.Document(MY_DIR + "Images.docx")

        # Get the collection of shapes from the document,
        # and save the image data of every shape with an image as a file to the local file system.
        shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)

        self.assertEqual(9, len([s for s in shapes if s.as_shape().has_image]))

        image_index = 0
        for shape in shapes:
            shape = shape.as_shape()

            if shape.has_image:

                # The image data of shapes may contain images of many possible image formats.
                # We can determine a file extension for each image automatically, based on its format.
                image_file_name = f"File.extract_images.{image_index}{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
                shape.image_data.save(ARTIFACTS_DIR + image_file_name)
                image_index += 1

        #ExEnd

        self.assertEqual(9, len([name for name in glob.glob(ARTIFACTS_DIR + "File.extract_images*.*")
                                 if os.path.splitext(name)[-1] in ['.jpeg', '.png', '.emf', '.wmf']]))
