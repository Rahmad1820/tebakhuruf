import random

def choose_word():
    words = ["python", "programming", "computer", "science", "coding", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Selamat datang di Game Tebak Huruf!")
    word_to_guess = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Kata: {current_display}")
        guess = input("Tebak huruf: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Anda sudah menebak huruf ini sebelumnya. Coba lagi.")
            elif guess in word_to_guess:
                print("Tebakan benar!")
                guessed_letters.append(guess)
            else:
                print("Tebakan salah. Coba lagi.")
                attempts += 1
        else:
            print("Masukkan hanya satu huruf. Coba lagi.")

        if set(word_to_guess) == set(guessed_letters):
            print(f"Selamat! Anda berhasil menebak kata: {word_to_guess}")
            break

    if attempts == max_attempts:
        print(f"Anda kalah! Kata yang benar adalah: {word_to_guess}")

if __name__ == "__main__":
    main()
