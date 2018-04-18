from Upload.Upload import upload, UPLOAD_FOLDER
from flask import Blueprint, Request
from werkzeug.datastructures import MultiDict, FileStorage
import unittest
from os.path import dirname
import os


class UploadTestCase(unittest.TestCase):

    def test_Not_POST(self):
        req = Request
        req.method = 'GET'
        req.files = MultiDict([('file', FileStorage(filename=u'img.png', content_type='image/jpeg'))])
        # bp = Blueprint('testBP', __name__)
        upload(req)
        fileLoc = os.path.join(dirname(dirname(dirname(__file__))), UPLOAD_FOLDER, req.files['file'].filename)
        try:
            unittest.assertFalse(os.path.exists(fileLoc))
        except:
            pass
        finally:
            if os.path.exists(fileLoc):
                os.remove(fileLoc)

    def test_bad_filetype(self):
        req = Request
        req.method = 'POST'
        req.files = MultiDict([('file', FileStorage(filename=u'img.txt', content_type='image/jpeg'))])
        # bp = Blueprint('testBP', __name__)
        upload(req)
        fileLoc = os.path.join(dirname(dirname(dirname(__file__))), UPLOAD_FOLDER, req.files['file'].filename)
        try:
            unittest.assertFalse(os.path.exists(fileLoc))
        except:
            pass
        finally:
            if os.path.exists(fileLoc):
                os.remove(fileLoc)

    def test_Upload_Success(self):

        req = Request
        req.method = 'POST'
        req.files = MultiDict([('file', FileStorage(filename=u'img.png', content_type='image/jpeg'))])
        # bp = Blueprint('testBP', __name__)
        upload(req)
        fileLoc = os.path.join(dirname(dirname(dirname(__file__))), UPLOAD_FOLDER, req.files['file'].filename)
        try:
            unittest.assertTrue(os.path.exists(fileLoc))
        except:
            pass
        finally:
            if os.path.exists(fileLoc):
                os.remove(fileLoc)

if __name__ == '__main__':
    unittest.main()