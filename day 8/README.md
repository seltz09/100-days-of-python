# Caesar Cipher 🔐

A Python implementation of the classic Caesar Cipher encryption technique, built as part of Day 8 of the 100 Days of Python challenge.

## Overview

The Caesar Cipher is one of the oldest and simplest encryption methods. It works by shifting each letter in the alphabet by a fixed number of positions. This program allows you to both encode (encrypt) and decode (decrypt) messages using any shift value you choose.

## How It Works

- **Encoding**: Each letter is shifted forward in the alphabet by your chosen number
- **Decoding**: Each letter is shifted backward in the alphabet by your chosen number
- **Wrap-around**: If shifting goes past 'z', it wraps back to 'a' (and vice versa)

### Example
- **Original**: "hello"
- **Shift by 3**: "khoor"
- **Shift by 5**: "mjqqt"

## Features

- **Bidirectional encryption** - Encode and decode messages
- **Any shift value** - Use any number for your cipher key
- **Preserves formatting** - Spaces, punctuation, and numbers remain unchanged
- **Continuous operation** - Encrypt/decrypt multiple messages in one session
- **Case handling** - Converts input to lowercase for consistency

## How to Use

1. **Run the program**
   ```bash
   python main.py
   ```

2. **Choose operation**
   - Type `encode` to encrypt a message
   - Type `decode` to decrypt a message

3. **Enter your message**
   - Type the text you want to encrypt/decrypt

4. **Set shift amount**
   - Enter a number for how many positions to shift

5. **View results**
   - See your encoded/decoded message

6. **Continue or exit**
   - Type `yes` to encrypt/decrypt another message
   - Type `no` to exit the program

## Sample Usage

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello world!

Type the shift number:
3

Here is the encoded result: khoor zruog!

Type 'yes' if you want to continue or 'no' to exit: yes

Type 'encode' to encrypt, type 'decode' to decrypt:
decode

Type your message:
khoor zruog!

Type the shift number:
3

Here is the decoded result: hello world!

Type 'yes' if you want to continue or 'no' to exit: no
See ya!
```

## Requirements

- Python 3.x
- Alphabet list defined as: `alphabet = ['a', 'b', 'c', ..., 'z']`

## File Structure

```
caesar-cipher/
│
├── main.py            # Main program file with game logic
├── art.py             # ASCII art and visual elements
└── README.md          # This file
```

## Code Structure

### Main Function
```python
def caesar(original_text, shift_amount, encode_or_decode):
    # Handles the encryption/decryption logic
```

### Main Loop
- Continuous program execution
- User input handling
- Function calls and result display

## Learning Objectives (Day 8)

This project reinforces several key Python concepts:

- **Functions with parameters** - Passing multiple arguments
- **String manipulation** - Character-by-character processing
- **List operations** - Finding indices and accessing elements
- **Modulo arithmetic** - Wrapping around the alphabet
- **Conditional logic** - Encoding vs decoding paths
- **Loops** - Processing each character and program continuation
- **User input validation** - Handling different input types

## Security Note

⚠️ **Educational Purpose Only**: The Caesar Cipher is extremely weak by modern standards and can be easily broken. This implementation is for learning programming concepts, not for securing sensitive information.

## Common Shift Values

- **ROT13** (shift by 13) - Popular variant used in forums
- **Shift by 1** - Simplest form (A→B, B→C, etc.)
- **Shift by 25** - Equivalent to shift by -1

## Historical Context

The Caesar Cipher is named after Julius Caesar, who reportedly used it to communicate with his generals around 50 BC. He typically used a shift of 3, which is why this value is sometimes called the "Caesar shift."

---

**Part of 100 Days of Python Challenge - Day 8**

*Built with Python 3 | Focus: Functions and Parameters*
