# Secret Snowflake

Allows a group of friends (>2 people) to have coordinate a secret snowflake exchange. Takes in a txt file with the participants' name and emails, then creates matches and emails each participant the person that they are supposed to get a gift for.

## Install required packages.
pip install -r requirements.txt

## Allow Secret Snowflake to send emails.
Create a .env file with the username and password of the gmail address used to contact participants. See sample.env for an example.env file.

Allow less secure apps to access this gmail account. For more detailed instructions, see this link: https://support.google.com/accounts/answer/6010255.

If you have 2-step verification, then you will need an app-specific password. For more detailed instructions, see this link: https://support.google.com/accounts/answer/185833.

## Usage
python3 secret_snowflake.py input_file.txt

Each line in the input file should be formatted 'Name, email'. See sample_input.txt for an example input file.