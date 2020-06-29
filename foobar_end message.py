

import base64

MESSAGE ='''HEUUFBEVDAcRT0FORU0GQlQGFkBNUlEKGw4EBBUCHwQXEV1CQAQBAgwRDw0FU0lKRlVXAQ0VFQFR SU5CTwgaBhgEVFgFDgJGXlZOFQEACBETDwxVXxNFR1tSURwaDgcCHwAORhwRQBAGAxAfHQdFSFtU QhkAVlRATkdGFBkGU0JSQVMSAw8RFho='''


KEY = 'gbgarvitbhateja01'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
