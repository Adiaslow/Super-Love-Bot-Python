from instapy_cli import client

            
username = 'superlovebot' #your username

password = 'Peace005!' #your password 

image = '/Users/Adam/Desktop/Super Love Bot/pil_text_font.png' #here you can put the image directory

text = 'Test' + '\r\n' + '#love #instagood'

with client(username, password) as cli:
    
    cli.upload(image, text)
