# Read from the file file.txt and output all valid phone numbers to stdout.
# regex for 987-123-4567 ^[0-9]{3}-[0-9]{3}-[0-9]{4}$
# regex for (123) 456-7890 ^\([0-9]{3,3}\) [0-9]{3}-[0-9]{4}$
cat file.txt | grep -E "(^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3,3}\) [0-9]{3}-[0-9]{4}$)"
