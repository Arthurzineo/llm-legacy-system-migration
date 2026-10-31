"""The memory diagnostic must never claim MCP tool readiness from HTTP reachability."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from ai_memory_doctor import diagnose

class Response:
    status=200
    def __enter__(self):return self
    def __exit__(self,*args):return False
    def read(self,n):return b'{"status":"ok"}'

class DoctorTest(unittest.TestCase):
    @patch('ai_memory_doctor.shutil.which',return_value=None)
    @patch('ai_memory_doctor.urllib.request.urlopen',return_value=Response())
    def test_http_is_not_mcp_ready(self,request,which):
        result=diagnose()
        self.assertEqual(result['server'],'healthy')
        self.assertEqual(result['binary'],'missing')
        self.assertEqual(result['client_mcp'],'requires_in_client_memory_status_call')
        self.assertFalse(result['ready'])

    def test_rejects_url_credentials(self):
        with self.assertRaises(ValueError):diagnose(server_url='http://user:secret@example.com')

if __name__=='__main__':unittest.main()
