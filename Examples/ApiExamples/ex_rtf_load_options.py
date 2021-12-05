import unittest
import io

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExRtfLoadOptions(ApiExampleBase):

    def test_recognize_utf8_text(self):

        for recognize_utf8_text in (False, True):
            with self.subTest(recognize_utf8_text=recognize_utf8_text):
                #ExStart
                #ExFor:RtfLoadOptions
                #ExFor:RtfLoadOptions.#ctor
                #ExFor:RtfLoadOptions.RecognizeUtf8Text
                #ExSummary:Shows how to detect UTF-8 characters while loading an RTF document.
                # Create an "RtfLoadOptions" object to modify how we load an RTF document.
                load_options = aw.loading.RtfLoadOptions()

                # Set the "recognize_utf8_text" property to "False" to assume that the document uses the ISO 8859-1 charset
                # and loads every character in the document.
                # Set the "recognize_utf8_text" property to "True" to parse any variable-length characters that may occur in the text.
                load_options.recognize_utf8_text = recognize_utf8_text

                doc = aw.Document(MY_DIR + "UTF-8 characters.rtf", load_options)

                if recognize_utf8_text:
                    self.assertEqual(
                        "“John Doe´s list of currency symbols”™\r" + "€, ¢, £, ¥, ¤",
                        doc.first_section.body.get_text().strip())
                else:
                    self.assertEqual(
                        "â€œJohn DoeÂ´s list of currency symbolsâ€\u009dâ„¢\r" + "â‚¬, Â¢, Â£, Â¥, Â¤",
                        doc.first_section.body.get_text().strip())
                #ExEnd
