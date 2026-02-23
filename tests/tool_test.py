import os
import unittest

from tools import chat


class ToolTestCase(unittest.TestCase):
    def test_invoke(self):
        api_key = os.getenv('AGENT_API_KEY')
        me = '45bdc865-6d71-40ab-8892-af53906362fa'
        base_url = "https://api.dify.ai/v1"
        rs = chat(base_url, api_key, me, "What are the specs of the iPhone 13 Pro Max?")

        print(rs)


if __name__ == '__main__':
    unittest.main()
