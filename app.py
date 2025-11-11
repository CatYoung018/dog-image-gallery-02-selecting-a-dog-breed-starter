from flask import Flask, render_template, request

import requests

<<<<<<< HEAD
=======
#imports a dictionary of data from dog_breeds.py and "prettifies", or styles, the dog names when they appear in the HTML page
>>>>>>> b29a8c5b21d36a943f5b8c95999247eb20dc0797
from dog_breeds import prettify_dog_breed

# Initialize the Flask application
app = Flask(__name__)

def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET","POST"])
def dog_images_gallery():
  errors = []
  if request.method == "POST":
    breed = request.form.get("breed")
    number = request.form.get("number")
    if not breed:
      errors.append("Oops! Please choose a breed.")
    if not number:
<<<<<<< HEAD
      errors.append("Oops! Please choose a number.")
    if breed and number:
=======
      errors.append("Oops! Please choose number.")
    if breed:
>>>>>>> b29a8c5b21d36a943f5b8c95999247eb20dc0797
      response = requests.get("https://dog.ceo/api/breed/" + check_breed(breed) + "/images/random/" + number)
      data = response.json()
      dog_images = data["message"]
      return render_template("dogs.html", images=dog_images, breed=prettify_dog_breed(breed), errors=[])
  return render_template("dogs.html", images=[], breed="", errors=errors)
<<<<<<< HEAD

@app.route("/random", methods=["POST"])
def get_random():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    dog_images = [data["message"]]
    return render_template("dogs.html", images=dog_images)

=======
>>>>>>> b29a8c5b21d36a943f5b8c95999247eb20dc0797


app.debug = True

# Run the flask server
if __name__ == "__main__":
    app.run()