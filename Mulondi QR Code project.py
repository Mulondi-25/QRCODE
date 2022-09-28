#!/usr/bin/env python
# coding: utf-8

# In[1]:



import qrcode


# In[3]:


def generate_qrcode(text):
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("Mulondi.png")


# In[6]:


generate_qrcode("Had a great time at the department of Public Works")

