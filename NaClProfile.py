# NaClProfile.py
# An encrypted version of the Profile class provided by the Profile.py module
# 
# for ICS 32
# by Mark S. Baldwin


# TODO: Install the pynacl library so that the following modules are available
# to your program.
import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from NaClDSEncoder import NaClDSEncoder
from Profile import Post
from Profile import Profile
import ds_client
import ds_protocol

# TODO: Import the Profile and Post classes
# TODO: Import the NaClDSEncoder module
    
# TODO: Subclass the Profile class

        
class NaClProfile(Profile):
    def __init__(self):#self, dsuserver, username, password):
        """
        TODO: Complete the initializer method. Your initializer should create the follow three 
        public data attributes:

        public_key:str
        private_key:str
        keypair:str

        Whether you include them in your parameter list is up to you. Your decision will frame 
        how you expect your class to be used though, so think it through.
        """
        
        self.public_key = ""
        self.private_key = ""
        self.keypair = ""
        super().__init__()
        
    def generate_keypair(self) -> str:
        """
        Generates a new public encryption key using NaClDSEncoder.

        TODO: Complete the generate_keypair method.

        This method should use the NaClDSEncoder module to generate a new keypair and populate
        the public data attributes created in the initializer.

        :return: str    
        """

        my_keys = NaClDSEncoder()
        my_keys.generate()
        self.keypair = my_keys.keypair
        self.public_key = my_keys.public_key
        self.private_key = my_keys.private_key
        
        return self.keypair
    
    def import_keypair(self, keypair: str):
        """
        Imports an existing keypair. Useful when keeping encryption keys in a location other than the
        dsu file created by this class.

        TODO: Complete the import_keypair method.

        This method should use the keypair parameter to populate the public data attributes created by
        the initializer. 
        
        NOTE: you can determine how to split a keypair by comparing the associated data attributes generated
        by the NaClDSEncoder
        """
        self.keypair = keypair
        self.public_key = keypair[:44]
        self.private_key = keypair[45:]


        """

    TODO: Override the add_post method to encrypt post entries.

    Before a post is added to the profile, it should be encrypted. Remember to take advantage of the
    code that is already written in the parent class.

    NOTE: To call the method you are overriding as it exists in the parent class, you can use the built-in super keyword:
    
    super().add_post(...)
    """

    def add_post(post):
    
        my_keys = NaClDSEncoder()
        encPublicKey = my_keys.encode_public_key(self.public_key)
        encPrivateKey = my_keys.encode_private_key(self.private_key)
        encoded_message = message.encode(encoding='utf-8')
        encryption_box = Box(encPrivateKey, encPublicKey)
        encrypted_message = encryption_box.encrypt(encoded_message, encoder=encoding.Base64Encoder)
        post.set_entry(encrypted_message.decode('utf-8'))
        super().add_post(post)

        return post
    

    """
    TODO: Override the get_posts method to decrypt post entries.

    Since posts will be encrypted when the add_post method is used, you will need to ensure they are 
    decrypted before returning them to the calling code.

    :return: Post
    
    NOTE: To call the method you are overriding as it exists in the parent class you can use the built-in super keyword:
    super().get_posts()
    """

    def get_posts(self):
        my_keys = NaClDSEncoder()
        DecPublicKey = my_keys.encode_public_key(self.public_key)
        DecPrivateKey = my_keys.encode_private_key(self.private_key)
        decrypted_message = encrypted_message.decode('utf-8')
        decrypted_message = boxed_keys.decrypt(encrypted_message, encoder=encoding.Base64Encoder)
        decryption_box = Box(DecPrivateKey, DecPublicKey)
        decoded_message = decrypted_message.decode(encoding='utf-8')
        encrypted_entries = super().get_posts()
        decrypted_entries = []

        for item in encryped_entries:
            new_item = Post(item['entry'])
            encrypted_message = new_item['entry']
            encrypted_message = encrypted_message.encode('utf-8')
            decryption_message = decryption_box.decrypt(encrypted_message, encoder=encoding.Base64Encoder)
            new_item.set_entry(decryption_message.decode('utf-8'))
            decrypted_entries.append(new_item)

        return decrypted_entries

    
    """
    TODO: Override the load_profile method to add support for storing a keypair.

    Since the DS Server is now making use of encryption keys rather than username/password attributes, you will 
    need to add support for storing a keypair in a dsu file. The best way to do this is to override the 
    load_profile module and add any new attributes you wish to support.

    NOTE: The Profile class implementation of load_profile contains everything you need to complete this TODO.
     Just copy the code here and add support for your new attributes.
    """

    def load_profile(self, path):
        p = Path(path)

        if os.path.exists(p) and p.suffix == '.dsu':
            try:
                f = open(p, 'r')
                obj = json.load(f)
                self.username = obj['username']
                self.password = obj['password']
                self.dsuserver = obj['dsuserver']
                self.bio = obj['bio']
                for post_obj in obj['_posts']:
                    post = Post(post_obj['entry'], post_obj['timestamp'])
                    self._posts.append(post)
                self.keypair = obj['keypair']
                self.private_key = obj['private key']
                self.public_key = obj['public key']
                f.close()
            except Exception as ex:
                raise DsuProfileError(ex)
        else:
            raise DsuFileError()

    def encrypt_entry(self, entry:str, public_key:str) -> bytes:
        """
        Used to encrypt messages using a 3rd party public key, such as the one that
        the DS server provides.
        
        TODO: Complete the encrypt_entry method.

        NOTE: A good design approach might be to create private encrypt and decrypt methods that your add_post, 
        get_posts and this method can call.
        
        :return: bytes 
        """

        entry_encode = entry.encode('utf-8')
        my_keys = NaClDSEncoder()
        private_key_encode = my_keys.encode_private_key(PrivateKey)
        public_key_encode = my_keys.encode_public_key(PublicKey)
        box = Box(private_key_encode, public_key_encode)
        box_encrypt = box.encrypt(entry_encode, encoder=encoding.Base64Encoder)
        

        
