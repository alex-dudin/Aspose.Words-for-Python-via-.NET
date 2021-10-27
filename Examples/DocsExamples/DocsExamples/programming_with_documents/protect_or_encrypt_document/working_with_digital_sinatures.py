from datetime import datetime
import uuid

import aspose.words as aw
from docs_examples_base import DocsExamplesBase, MY_DIR, ARTIFACTS_DIR, IMAGES_DIR

class WorkingWithDigitalSinatures(DocsExamplesBase):

    def test_sign_document(self):

        #ExStart:SingDocument
        cert_holder = aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw")

        aw.digitalsignatures.DigitalSignatureUtil.sign(MY_DIR + "Digitally signed.docx", ARTIFACTS_DIR + "Document.signed.docx", cert_holder)
        #ExEnd:SingDocument

    def test_signing_encrypted_document(self):

        #ExStart:SigningEncryptedDocument
        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.decryption_password = "decryptionPassword"

        cert_holder = aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw")

        aw.digitalsignatures.DigitalSignatureUtil.sign(MY_DIR + "Digitally signed.docx",
            ARTIFACTS_DIR + "Document.encrypted_document.docx", cert_holder, sign_options)
        #ExEnd:SigningEncryptedDocument

    def test_creating_and_signing_new_signature_line(self):

        #ExStart:CreatingAndSigningNewSignatureLine
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        signature_line = builder.insert_signature_line(aw.SignatureLineOptions()).signature_line

        doc.save(ARTIFACTS_DIR + "SignDocuments.signature_line.docx")

        sign_options = aw.digitalsignatures.SignOptions()

        sign_options.signature_line_id = signature_line.id
        with open(IMAGES_DIR + "Enhanced Windows MetaFile.emf", "rb") as image_file:
            sign_options.signature_line_image = image_file.read()

        cert_holder = aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw")

        aw.digitalsignatures.DigitalSignatureUtil.sign(ARTIFACTS_DIR + "SignDocuments.signature_line.docx",
            ARTIFACTS_DIR + "SignDocuments.new_signature_line.docx", cert_holder, sign_options)
        #ExEnd:CreatingAndSigningNewSignatureLine

    def test_signing_existing_signature_line(self):

        #ExStart:SigningExistingSignatureLine
        doc = aw.Document(MY_DIR + "Signature line.docx")

        signature_line = doc.first_section.body.get_child(aw.NodeType.SHAPE, 0, True).as_shape().signature_line

        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.signature_line_id = signature_line.id

        with open(IMAGES_DIR + "Enhanced Windows MetaFile.emf", "rb") as image_file:
            sign_options.signature_line_image = image_file.read()

        cert_holder = aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw")

        aw.digitalsignatures.DigitalSignatureUtil.sign(MY_DIR + "Digitally signed.docx",
            ARTIFACTS_DIR + "SignDocuments.signing_existing_signature_line.docx", cert_holder, sign_options)
        #ExEnd:SigningExistingSignatureLine

    def test_set_signature_provider_id(self):

        #ExStart:SetSignatureProviderID
        doc = aw.Document(MY_DIR + "Signature line.docx")

        signature_line = doc.first_section.body.get_child(aw.NodeType.SHAPE, 0, True).as_shape().signature_line

        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.provider_id = signature_line.provider_id
        sign_options.signature_line_id = signature_line.id

        cert_holder = aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw")

        aw.digitalsignatures.DigitalSignatureUtil.sign(MY_DIR + "Digitally signed.docx",
            ARTIFACTS_DIR + "SignDocuments.set_signature_provider_id.docx", cert_holder, sign_options)
        #ExEnd:SetSignatureProviderID

    def test_create_new_signature_line_and_set_provider_id(self):

        #ExStart:CreateNewSignatureLineAndSetProviderID
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        signature_line_options = aw.SignatureLineOptions()
        signature_line_options.signer = "vderyushev"
        signature_line_options.signer_title = "QA"
        signature_line_options.email = "vderyushev@aspose.com"
        signature_line_options.show_date = True
        signature_line_options.default_instructions = False
        signature_line_options.instructions = "Please sign here."
        signature_line_options.allow_comments = True

        signature_line = builder.insert_signature_line(signature_line_options).signature_line
        signature_line.provider_id = uuid.UUID('{CF5A7BB4-8F3C-4756-9DF6-BEF7F13259A2}')

        doc.save(ARTIFACTS_DIR + "SignDocuments.signature_line_provider_id.docx")

        sign_options = aw.digitalsignatures.SignOptions()
        sign_options.signature_line_id = signature_line.id
        sign_options.provider_id = signature_line.provider_id
        sign_options.comments = "Document was signed by vderyushev"
        sign_options.sign_time = datetime.now()

        cert_holder = aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw")

        aw.digitalsignatures.DigitalSignatureUtil.sign(ARTIFACTS_DIR + "SignDocuments.signature_line_provider_id.docx",
            ARTIFACTS_DIR + "SignDocuments.create_new_signature_line_and_set_provider_id.docx", cert_holder, sign_options)
        #ExEnd:CreateNewSignatureLineAndSetProviderID


    def test_access_and_verify_signature(self):

        #ExStart:AccessAndVerifySignature
        doc = aw.Document(MY_DIR + "Digitally signed.docx")

        for signature in doc.digital_signatures:
            print("*** Signature Found ***")
            print("Is valid: " + str(signature.is_valid))
            # This property is available in MS Word documents only.
            print("Reason for signing: " + signature.comments)
            print("Time of signing: " + str(signature.sign_time))

        #ExEnd:AccessAndVerifySignature

            # Currently certificate property is not available in Python.
            #print("Subject name: " + signature.certificate_holder.certificate.subject_name.name)
            #print("Issuer name: " + signature.certificate_holder.certificate.issuer_name.name)
