# Copyright (c) 2001-2022 Aspose Pty Ltd. All Rights Reserved.
#
# This file is part of Aspose.Words. The source code in this file
# is only intended as a supplement to the documentation, and is provided
# "as is", without warranty of any kind, either expressed or implied.

import datetime
import os
from typing import List

import aspose.words as aw

from api_example_base import ApiExampleBase, MY_DIR, ARTIFACTS_DIR, FONTS_DIR, IMAGE_DIR

class ExLoadOptions(ApiExampleBase):

    ##ExStart
    ##ExFor:LoadOptions.resource_loading_callback
    ##ExSummary:Shows how to handle external resources when loading Html documents.
    #def test_load_options_callback(self):

    #    load_options = aw.loading.LoadOptions()
    #    load_options.resource_loading_callback = ExLoadOptions.HtmlLinkedResourceLoadingCallback()

    #    # When we load the document, our callback will handle linked resources such as CSS stylesheets and images.
    #    doc = aw.Document(MY_DIR + "Images.html", load_options)
    #    doc.save(ARTIFACTS_DIR + "LoadOptions.load_options_callback.pdf")

    #class HtmlLinkedResourceLoadingCallback(aw.loading.IResourceLoadingCallback):
    #    """Prints the filenames of all external stylesheets and substitutes all images of a loaded html document."""

    #    def resource_loading(self, args: aw.loading.ResourceLoadingArgs) -> aw.loading.ResourceLoadingAction:

    #        if args.resource_type == aw.loading.ResourceType.CSS_STYLE_SHEET:
    #            print(f"External CSS Stylesheet found upon loading: {args.original_uri}")
    #            return aw.loading.ResourceLoadingAction.DEFAULT

    #        elif args.resource_type == aw.loading.ResourceType.IMAGE:
    #            print(f"External Image found upon loading: {args.original_uri}")

    #            new_image_filename = "Logo.jpg"
    #            print(f"\tImage will be substituted with: {new_image_filename}")

    #            new_image = drawing.Image.from_file(IMAGE_DIR + new_image_filename)

    #            converter = drawing.ImageConverter()
    #            image_bytes = converter.convert_to(new_image, type(bytes))
    #            args.set_data(image_bytes)

    #            return aw.loading.ResourceLoadingAction.USER_PROVIDED

    #        return aw.loading.ResourceLoadingAction.DEFAULT

    ##ExEnd

    def test_convert_shape_to_office_math(self):

        for is_convert_shape_to_office_math in (True, False):
            with self.subTest(is_convert_shape_to_office_math=is_convert_shape_to_office_math):
                #ExStart
                #ExFor:LoadOptions.convert_shape_to_office_math
                #ExSummary:Shows how to convert EquationXML shapes to Office Math objects.
                load_options = aw.loading.LoadOptions()

                # Use this flag to specify whether to convert the shapes with EquationXML attributes
                # to Office Math objects and then load the document.
                load_options.convert_shape_to_office_math = is_convert_shape_to_office_math

                doc = aw.Document(MY_DIR + "Math shapes.docx", load_options)

                if is_convert_shape_to_office_math:
                    self.assertEqual(16, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
                    self.assertEqual(34, doc.get_child_nodes(aw.NodeType.OFFICE_MATH, True).count)
                else:
                    self.assertEqual(24, doc.get_child_nodes(aw.NodeType.SHAPE, True).count)
                    self.assertEqual(0, doc.get_child_nodes(aw.NodeType.OFFICE_MATH, True).count)

                #ExEnd

    def test_set_encoding(self):

        #ExStart
        #ExFor:LoadOptions.encoding
        #ExSummary:Shows how to set the encoding with which to open a document.
        # A FileFormatInfo object will detect this file as being encoded in something other than UTF-7.
        file_format_info = aw.FileFormatUtil.detect_file_format(MY_DIR + "Encoded in UTF-7.txt")

        self.assertNotEqual("utf-7", file_format_info.encoding)

        # If we load the document with no loading configurations, Aspose.Words will detect its encoding as UTF-8.
        doc = aw.Document(MY_DIR + "Encoded in UTF-7.txt")

        # The contents, parsed in UTF-8, create a valid string.
        # However, knowing that the file is in UTF-7, we can see that the result is incorrect.
        self.assertEqual("Hello world+ACE-", doc.to_string(aw.SaveFormat.TEXT).strip())

        # In cases of ambiguous encoding such as this one, we can set a specific encoding variant
        # to parse the file within a LoadOptions object.
        load_options = aw.loading.LoadOptions()
        load_options.encoding = "utf-7"

        # Load the document while passing the LoadOptions object, then verify the document's contents.
        doc = aw.Document(MY_DIR + "Encoded in UTF-7.txt", load_options)

        self.assertEqual("Hello world!", doc.to_string(aw.SaveFormat.TEXT).strip())
        #ExEnd

    def test_font_settings(self):

        #ExStart
        #ExFor:LoadOptions.font_settings
        #ExSummary:Shows how to apply font substitution settings while loading a document.
        # Create a FontSettings object that will substitute the "Times New Roman" font
        # with the font "Arvo" from our "MyFonts" folder.
        font_settings = aw.fonts.FontSettings()
        font_settings.set_fonts_folder(FONTS_DIR, False)
        font_settings.substitution_settings.table_substitution.add_substitutes("Times New Roman", "Arvo")

        # Set that FontSettings object as a property of a newly created LoadOptions object.
        load_options = aw.loading.LoadOptions()
        load_options.font_settings = font_settings

        # Load the document, then render it as a PDF with the font substitution.
        doc = aw.Document(MY_DIR + "Document.docx", load_options)

        doc.save(ARTIFACTS_DIR + "LoadOptions.font_settings.pdf")
        #ExEnd

    def test_load_options_msw_version(self):

        #ExStart
        #ExFor:LoadOptions.msw_version
        #ExSummary:Shows how to emulate the loading procedure of a specific Microsoft Word version during document loading.
        # By default, Aspose.Words load documents according to Microsoft Word 2019 specification.
        load_options = aw.loading.LoadOptions()

        self.assertEqual(aw.settings.MsWordVersion.WORD2019, load_options.msw_version)

        # This document is missing the default paragraph formatting style.
        # This default style will be regenerated when we load the document either with Microsoft Word or Aspose.Words.
        load_options.msw_version = aw.settings.MsWordVersion.WORD2007
        doc = aw.Document(MY_DIR + "Document.docx", load_options)

        # The style's line spacing will have this value when loaded by Microsoft Word 2007 specification.
        self.assertAlmostEqual(12.95, doc.styles.default_paragraph_format.line_spacing, delta=0.01)
        #ExEnd

    ##ExStart
    ##ExFor:LoadOptions.warning_callback
    ##ExSummary:Shows how to print and store warnings that occur during document loading.
    #def test_load_options_warning_callback(self):

    #    # Create a new LoadOptions object and set its WarningCallback attribute
    #    # as an instance of our IWarningCallback implementation.
    #    load_options = aw.loading.LoadOptions()
    #    load_options.warning_callback = ExLoadOptions.DocumentLoadingWarningCallback()

    #    # Our callback will print all warnings that come up during the load operation.
    #    doc = aw.Document(MY_DIR + "Document.docx", load_options)

    #    warnings = load_options.warning_callback.warnings
    #    self.assertEqual(3, warnings.count)
    #    self._test_load_options_warning_callback(warnings) #ExSkip

    #class DocumentLoadingWarningCallback(aw.IWarningCallback):
    #    """IWarningCallback that prints warnings and their details as they arise during document loading."""

    #    def __init__(self):
    #        self.warnings: List[aw.WarningInfo] = []

    #    def warning(self, info: aw.WarningInfo):

    #        print(f"Warning: {info.warning_type}")
    #        print(f"\tSource: {info.source}")
    #        print(f"\tDescription: {info.description}")
    #        self.warnings.add(info)

    ##ExEnd

    def _test_load_options_warning_callback(self, warnings: List[aw.WarningInfo]):

        self.assertEqual(aw.WarningType.UNEXPECTED_CONTENT, warnings[0].warning_type)
        self.assertEqual(aw.WarningSource.DOCX, warnings[0].source)
        self.assertEqual("3F01", warnings[0].description)

        self.assertEqual(aw.WarningType.MINOR_FORMATTING_LOSS, warnings[1].warning_type)
        self.assertEqual(aw.WarningSource.DOCX, warnings[1].source)
        self.assertEqual("Import of element 'shapedefaults' is not supported in Docx format by Aspose.words.", warnings[1].description)

        self.assertEqual(aw.WarningType.MINOR_FORMATTING_LOSS, warnings[2].warning_type)
        self.assertEqual(aw.WarningSource.DOCX, warnings[2].source)
        self.assertEqual("Import of element 'extraClrSchemeLst' is not supported in Docx format by Aspose.words.", warnings[2].description)

    def test_temp_folder(self):

        #ExStart
        #ExFor:LoadOptions.temp_folder
        #ExSummary:Shows how to use the hard drive instead of memory when loading a document.
        # When we load a document, various elements are temporarily stored in memory as the save operation occurs.
        # We can use this option to use a temporary folder in the local file system instead,
        # which will reduce our application's memory overhead.
        options = aw.loading.LoadOptions()
        options.temp_folder = ARTIFACTS_DIR + "TempFiles"

        # The specified temporary folder must exist in the local file system before the load operation.
        os.makedirs(options.temp_folder, exist_ok=True)

        doc = aw.Document(MY_DIR + "Document.docx", options)

        # The folder will persist with no residual contents from the load operation.
        self.assertListEqual([], os.listdir(options.temp_folder))
        #ExEnd

    def test_add_editing_language(self):

        #ExStart
        #ExFor:LanguagePreferences
        #ExFor:LanguagePreferences.add_editing_language(EditingLanguage)
        #ExFor:LoadOptions.language_preferences
        #ExFor:EditingLanguage
        #ExSummary:Shows how to apply language preferences when loading a document.
        load_options = aw.loading.LoadOptions()
        load_options.language_preferences.add_editing_language(aw.loading.EditingLanguage.JAPANESE)

        doc = aw.Document(MY_DIR + "No default editing language.docx", load_options)

        locale_id_far_east = doc.styles.default_font.locale_id_far_east
        if locale_id_far_east == aw.loading.EditingLanguage.JAPANESE:
            print("The document either has no any FarEast language set in defaults or it was set to Japanese originally.")
        else:
            print("The document default FarEast language was set to another than Japanese language originally, so it is not overridden.")
        #ExEnd

        self.assertEqual(aw.loading.EditingLanguage.JAPANESE, doc.styles.default_font.locale_id_far_east)

        doc = aw.Document(MY_DIR + "No default editing language.docx")

        self.assertEqual(aw.loading.EditingLanguage.ENGLISH_US, doc.styles.default_font.locale_id_far_east)

    def test_set_editing_language_as_default(self):

        #ExStart
        #ExFor:LanguagePreferences.default_editing_language
        #ExSummary:Shows how set a default language when loading a document.
        load_options = aw.loading.LoadOptions()
        load_options.language_preferences.default_editing_language = aw.loading.EditingLanguage.RUSSIAN

        doc = aw.Document(MY_DIR + "No default editing language.docx", load_options)

        locale_id = doc.styles.default_font.locale_id
        if locale_id == aw.loading.EditingLanguage.RUSSIAN:
            print("The document either has no any language set in defaults or it was set to Russian originally.")
        else:
            print("The document default language was set to another than Russian language originally, so it is not overridden.")
        #ExEnd

        self.assertEqual(aw.loading.EditingLanguage.RUSSIAN, doc.styles.default_font.locale_id)

        doc = aw.Document(MY_DIR + "No default editing language.docx")

        self.assertEqual(aw.loading.EditingLanguage.ENGLISH_US, doc.styles.default_font.locale_id)

    def test_convert_metafiles_to_png(self):

        #ExStart
        #ExFor:LoadOptions.convert_metafiles_to_png
        #ExSummary:Shows how to convert WMF/EMF to PNG during loading document.
        doc = aw.Document()

        shape = aw.drawing.Shape(doc, aw.drawing.ShapeType.IMAGE)
        shape.image_data.set_image(IMAGE_DIR + "Windows MetaFile.wmf")
        shape.width = 100
        shape.height = 100

        doc.first_section.body.first_paragraph.append_child(shape)

        doc.save(ARTIFACTS_DIR + "Image.convert_metafiles_to_png.docx")

        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()

        self.verify_image_in_shape(1600, 1600, aw.drawing.ImageType.WMF, shape)

        load_options = aw.loading.LoadOptions()
        load_options.convert_metafiles_to_png = True

        doc = aw.Document(ARTIFACTS_DIR + "Image.convert_metafiles_to_png.docx", load_options)
        shape = doc.get_child(aw.NodeType.SHAPE, 0, True).as_shape()

        self.verify_image_in_shape(1666, 1666, aw.drawing.ImageType.PNG, shape)
        #ExEnd

    def test_open_chm_file(self):

        info = aw.FileFormatUtil.detect_file_format(MY_DIR + "HTML help.chm")
        self.assertEqual(info.load_format, aw.LoadFormat.CHM)

        load_options = aw.loading.LoadOptions()
        load_options.encoding = "windows-1251"

        doc = aw.Document(MY_DIR + "HTML help.chm", load_options)

    ##ExStart
    ##ExFor:LoadOptions.progress_callback
    ##ExFor:IDocumentLoadingCallback
    ##ExFor:IDocumentLoadingCallback.notify
    ##ExSummary:Shows how to notify the user if document loading exceeded expected loading time.
    #def test_progressCallback(self):
    #
    #    progress_callback = ExLoadOptions.LoadingProgressCallback()
    #
    #    load_options = aw.LoadOptions()
    #    load_options.progress_callback = progress_callback
    #
    #    try:
    #        doc = aw.Document(MY_DIR + "Big document.docx", load_options)
    #    except OperationCanceledException as exception:
    #        print(exception)
    #        # Handle loading duration issue.
    #
    #class LoadingProgressCallback(aw.loading.IDocumentLoadingCallback):
    #    """Cancel a document loading after the "max_duration" seconds."""
    #
    #    def __init__(self):
    #        # Date and time when document loading is started.
    #        self.loading_started_at = datetime.datetime.now()
    #
    #        # Maximum allowed duration in sec.
    #        self.max_duration = 0.5
    #
    #    def notify(self, args: aw.loading.DocumentLoadingArgs):
    #        """Callback method which called during document loading.
    #        
    #        :param args: Loading arguments.
    #        """
    #        canceled_at = datetime.datetime.now()
    #        ellapsed_seconds = (canceled_at - self.loading_started_at).total_seconds()
    #
    #        if ellapsed_seconds > self.max_duration:
    #            raise OperationCanceledException(f"estimated_progress = {args.estimated_progress}; canceled_at = {canceled_at}")
    #
    ##ExEnd
