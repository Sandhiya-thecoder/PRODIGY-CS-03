import re

def password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length (at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters.")

    # Rule 2: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters.")

    # Rule 3: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters.")

    # Rule 4: Digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include numbers.")

    # Rule 5: Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Use special characters (e.g., !, @, #).")

    # Determine strength
    if score == 5:
        strength = "🔒 Strong"
    elif 3 <= score < 5:
        strength = "⚠️ Moderate"
    else:
        strength = "❌ Weak"

    return strength, feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, feedback = password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for msg in feedback:
            print(" -", msg)
    else:
        print("✅ Your password is strong!")
