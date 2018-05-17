import hashlib


def getHash(fileName):
    if fileName == 'elasticsearch-6.2.4.deb':
        return '0ccb8533af786d1659914341ab4481fef9dae99a515a9a789f128613bab42b4c3d3753a524810267e31707ef6c58e4b3c297501e8283b1da64138e9b26262119'
    elif fileName == 'kibana-6.2.4-linux-x86_64.tar.gz':
        return '125c2002e1a3b197f9f0d6200f2979f2e5974a902bfec2baa4b34a0c8d55babccafdb87b8a7b69c61ca4c02b8ae97e69b9b2743f7d445f0e53e31c69288296d5'
    elif fileName == 'kibana-6.2.4-linux-x86.tar.gz':
        return '47d7707b1b8feb490276fd69b597d27af610d28b'
    elif fileName == 'logstash-6.2.4.deb':
        return 'b30673aa23b8e150ba7136d0dd508bf1b6aa779a7a61af96279636fdc8010f0467446413b9a03591082f1d06666d6ae622ca1a409d4127a7c642fa2bb2773838'
    elif fileName == 'bro-2.5.3.tar.gz':
        return '45138464dcc8873409b84151a1393b7ec7206533686d31ab4a1fc1f22e83279ab105b70d8933b884526f4f411a05c0b6ca560cbdd6cdeccc05cc365604ea6210'
    return ''

def checkHash(fileName):
    BUF_SIZE = 65536
    sha512 = hashlib.sha512()
    with open(fileName, 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    sha512=sha512.hexdigest()
    if sha512 == getHash(fileName):
        return True
    else:
        return False