from tkinter import *
import random
from PIL import Image, ImageTk
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_window():

    root = Tk()
    root.title("Alexa Tell Me a Joke ")
    root.attributes('-fullscreen', True)
    root.config(bg="black")
    return root


root = setup_window()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


bg_image = Image.open(os.path.join(SCRIPT_DIR, "Alexbgimg.png"))
bg_image = bg_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo

jokes = [
    {"setup": "Why did the chicken cross the road?", "punchline": "To get to the other side."},
    {"setup": "What happens if you boil a clown?", "punchline": "You get a laughing stock."},
    {"setup": "Why did the car get a flat tire?", "punchline": "Because there was a fork in the road!"},
    {"setup": "How did the hipster burn his mouth?", "punchline": "He ate his pizza before it was cool."},
    {"setup": "What did the janitor say when he jumped out of the closet?", "punchline": "SUPPLIES!!!!"},
    {"setup": "Have you heard about the band 1023MB?", "punchline": "It's probably because they haven't got a gig yet…"},
    {"setup": "Why does the golfer wear two pants?", "punchline": "Because he's afraid he might get a \"Hole-in-one.\""},
    {"setup": "Why should you wear glasses to maths class?", "punchline": "Because it helps with division."},
    {"setup": "Why does it take pirates so long to learn the alphabet?", "punchline": "Because they could spend years at C."},
    {"setup": "Why did the woman go on the date with the mushroom?", "punchline": "Because he was a fun-ghi."},
    {"setup": "Why do bananas never get lonely?", "punchline": "Because they hang out in bunches."},
    {"setup": "What did the buffalo say when his kid went to college?", "punchline": "Bison."},
    {"setup": "Why shouldn't you tell secrets in a cornfield?", "punchline": "Too many ears."},
    {"setup": "What do you call someone who doesn't like carbs?", "punchline": "Lack-Toast Intolerant."},
    {"setup": "Why did the can crusher quit his job?", "punchline": "Because it was soda pressing."},
    {"setup": "Why did the birthday boy wrap himself in paper?", "punchline": "He wanted to live in the present."},
    {"setup": "What does a house wear?", "punchline": "A dress."},
    {"setup": "Why couldn't the toilet paper cross the road?", "punchline": "Because it got stuck in a crack."},
    {"setup": "Why didn't the bike want to go anywhere?", "punchline": "Because it was two-tired!"},
    {"setup": "Want to hear a pizza joke?", "punchline": "Nahhh, it's too cheesy!"},
    {"setup": "Why are chemists great at solving problems?", "punchline": "Because they have all of the solutions!"},
    {"setup": "Why is it impossible to starve in the desert?", "punchline": "Because of all the sand which is there!"},
    {"setup": "What did the cheese say when it looked in the mirror?", "punchline": "Halloumi!"},
    {"setup": "Why did the developer go broke?", "punchline": "Because he used up all his cache."},
    {"setup": "Did you know that ants are the only animals that don't get sick?", "punchline": "It's true! It's because they have little antibodies."},
    {"setup": "Why did the donut go to the dentist?", "punchline": "To get a filling."},
    {"setup": "What do you call a bear with no teeth?", "punchline": "A gummy bear!"},
    {"setup": "What does a vegan zombie like to eat?", "punchline": "Graaains."},
    {"setup": "What do you call a dinosaur with only one eye?", "punchline": "A Do-you-think-he-saw-us!"},
    {"setup": "Why should you never fall in love with a tennis player?", "punchline": "Because to them... love means NOTHING!"},
    {"setup": "What did the full glass say to the empty glass?", "punchline": "You look drunk."},
    {"setup": "What's a potato's favorite form of transportation?", "punchline": "The gravy train"},
    {"setup": "What did one ocean say to the other?", "punchline": "Nothing, they just waved."},
    {"setup": "What did the right eye say to the left eye?", "punchline": "Honestly, between you and me something smells."},
    {"setup": "What do you call a dog that's been run over by a steamroller?", "punchline": "Spot!"},
    {"setup": "What's the difference between a hippo and a zippo?", "punchline": "One's pretty heavy and the other's a little lighter"},
    {"setup": "Why don't scientists trust Atoms?", "punchline": "They make up everything."},
]

current_joke = None


def show_joke():
    global current_joke
    current_joke = random.choice(jokes)
    joke_label.config(text=current_joke["setup"])
    punchline_button.config(state="normal")
    Joke_button.pack_forget()


def show_punchline():
    joke_label.config(text=f"{current_joke['setup']}\n\n{current_joke['punchline']}")
    punchline_button.config(state="disabled")
    Joke_button.pack(pady=20)


main_frame = Frame(root, bg="#2d3f5f", highlightthickness=3, highlightbackground="#00d9ff")
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.6)


joke_box = Frame(main_frame, bg="#1a1f3a", highlightthickness=2, 
                highlightbackground="#00d9ff", relief="solid")
joke_box.pack(pady=20, padx=30, fill=BOTH, expand=True)

joke_label = Label(joke_box, text="Wanna Hear a Joke?", 
                  font=("Arial", 16), fg="white", bg="#1a1f3a", 
                  wraplength=400, justify=CENTER)
joke_label.pack(pady=30, padx=20)

Joke_button = Button(main_frame, text="Tell Me a Joke", command=show_joke,
                    font=("Arial", 14, "bold"), fg="white", bg="#001f3f",
                    cursor="hand2", bd=0, relief="flat", padx=30, pady=10)
Joke_button.pack(pady=10)

punchline_button = Button(main_frame, text="Show Punchline", command=show_punchline,
                         font=("Arial", 14, "bold"), fg="white", bg="#001f3f",
                         cursor="hand2", bd=0, relief="flat", padx=30, pady=10,
                         state="disabled")
punchline_button.pack(pady=10)

exit_button = Button(main_frame, text="Exit", command=root.destroy,
                    font=("Arial", 14, "bold"), fg="white", bg="#001f3f",
                    cursor="hand2", bd=0, relief="flat", padx=30, pady=10)
exit_button.pack(side=BOTTOM, pady=20)


root.mainloop()
