from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from sklearn.tree import DecisionTreeClassifier
import joblib
import base64
from .publickey import generate_and_save_public_key

GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)


class Data(models.Model):
    # name = models.CharField(max_length=100, null=True)
    # age = models.PositiveIntegerField(
    #     validators=[MinValueValidator(13), MaxValueValidator(19)], null=True)
    # height = models.PositiveIntegerField(null=True)
    # sex = models.PositiveIntegerField(choices=GENDER, null=True)
    # predictions = models.CharField(max_length=100, blank=True)
    # date = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, null=True)
    sex = models.PositiveIntegerField(choices=GENDER,null=True)
    Age = models.PositiveIntegerField( null=True)
    EDUC = models.PositiveIntegerField(null=True)
    SES=models.PositiveIntegerField(null=True)
    MMSE=models.PositiveIntegerField(null=True)
    eTIV=models.PositiveIntegerField(null=True)
    nWBV=models.FloatField(null=True)
    ASF=models.FloatField(null=True)
    predictions = models.PositiveIntegerField( blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # def encrypt_data(self, data):
    # # Ensure data is an integer
    #     if not isinstance(data, int):
    #         raise ValueError("Data must be an integer")

    # # Load the public key
    #     public_key_path = generate_and_save_public_key()
    #     with open(public_key_path, 'rb') as f:
    #         public_key = serialization.load_pem_public_key(
    #             f.read(),
    #             backend=default_backend()
    #     )

    # # Convert the integer to bytes before encryption
    #     data_bytes = data.to_bytes((data.bit_length() + 7) // 8, 'big')

    # # Encrypt the data using the public key
    #     ciphertext = public_key.encrypt(
    #         data_bytes,
    #         padding.OAEP(
    #             mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #             algorithm=hashes.SHA256(),
    #             label=None
    #     )
    # )
    #     return base64.b64encode(ciphertext).decode()

    
    # def encrypt_data(self, data):
    # # Convert integers to strings
    # if not isinstance(data, str):
    #     data = str(data)

    # # Load the public key
    # public_key_path = generate_and_save_public_key()
    # with open(public_key_path, 'rb') as f:
    #     public_key = serialization.load_pem_public_key(
    #         f.read(),
    #         backend=default_backend()
    #     )

    # # Encrypt the data using the public key
    # ciphertext = public_key.encrypt(
    #     data.encode('utf-8'),
    #     padding.OAEP(
    #         mgf=padding.MGF1(algorithm=hashes.SHA256()),
    #         algorithm=hashes.SHA256(),
    #         label=None
    #     )
    # )
    # return base64.b64encode(ciphertext).decode()


    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/xgboost.joblib')
        self.predictions = ml_model.predict(
            [[self.sex, self.Age, self.EDUC,self.SES,self.MMSE,self.eTIV,self.nWBV,self.ASF]])
        return super().save(*args, *kwargs)

    # def save(self, *args, **kwargs):
    # # Load the machine learning model
    #  ml_model = joblib.load('ml_model/xgboost.joblib')

    # # Encrypt sensitive data before passing to the model
    #  encrypted_data = [
    #     self.encrypt_data((self.sex)),
    #     self.encrypt_data((self.Age)),
    #     self.encrypt_data((self.EDUC)),
    #     self.encrypt_data((self.SES)),
    #     self.encrypt_data((self.MMSE)),
    #     self.encrypt_data((self.eTIV)),
    #     self.encrypt_data((self.nWBV)),
    #     self.encrypt_data((self.ASF)),
    # ]

    # # Make predictions
    #  self.predictions = ml_model.predict([encrypted_data])

    # # Save the object
    #  super().save(*args, **kwargs)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
