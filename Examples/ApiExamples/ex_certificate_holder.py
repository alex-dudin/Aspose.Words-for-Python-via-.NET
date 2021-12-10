import unittest
import io

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExCertificateHolder(ApiExampleBase):

    def test_create(self):

        #ExStart
        #ExFor:CertificateHolder.Create(Byte[], SecureString)
        #ExFor:CertificateHolder.Create(Byte[], String)
        #ExFor:CertificateHolder.Create(String, String, String)
        #ExSummary:Shows how to create CertificateHolder objects.
        # Below are four ways of creating CertificateHolder objects.
        # 1 -  Load a PKCS #12 file into a byte array and apply its password:
        with open(MY_DIR + "morzal.pfx", "rb") as file:
            cert_bytes = file.read()
        aw.digitalsignatures.CertificateHolder.create(cert_bytes, "aw")

        # 2 -  Load a PKCS #12 file into a byte array, and apply a secure password:
        password = NetworkCredential("", "aw").secure_password
        aw.digitalsignatures.CertificateHolder.create(cert_bytes, password)

        # If the certificate has private keys corresponding to aliases,
        # we can use the aliases to fetch their respective keys. First, we will check for valid aliases.
        with open(MY_DIR + "morzal.pfx", "rb") as cert_stream:
            pkcs12_store = Pkcs12Store(cert_stream, "aw")
            for alias in pkcs12_store.aliases:
                if pkcs12_store.is_key_entry(alias) and pkcs12_store.get_key(alias).key.is_private:
                    print(f"Valid alias found: {alias}")

        # 3 -  Use a valid alias:
        aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw", "c20be521-11ea-4976-81ed-865fbbfc9f24")

        # 4 -  Pass "null" as the alias in order to use the first available alias that returns a private key:
        aw.digitalsignatures.CertificateHolder.create(MY_DIR + "morzal.pfx", "aw", None)
        #ExEnd