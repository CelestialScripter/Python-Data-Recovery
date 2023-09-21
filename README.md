# Skype_recov
This utility can retrieve and convert deleted messages from the Skype app's database into text files, ensuring that they remain accessible.

## Installation
`pip3 install skype_recov `

OR 
- Clone the Repository:
  `https://github.com/CelestialScripter/Python-Data-Recovery  `
-Install dependencies using pip:
  `pip3 install -r requirements.txt`
-Install the package using setup.py:
  `python3 setup.py install`
## Usage
- Get the path of your main.db
`~/.Skype/USERNAME/main.db`
``` priest@mba:/media/priest/Downloads/skype_recov$ skype_recov --help
Usage: skype_recov [OPTIONS] FILE

Options:
  -s, --save TEXT  Path to save chats
  --help           Show this message and exit.

priest@mba:/media/priest/Downloads/skype_recov$ skype_recov ~/.Skype/MY_USERNAME/main.db
chat_896_other1_me.txt
chat_1536_me_other2.txt
chat_901_me_other3.txt
chat_2057_me_other4.txt
...

Files saved to .

```## Usage and Liability Disclaimer

**Usage Agreement:** The code contained in this repository should only be used with proper consent and in strict compliance with all applicable local, state, and federal laws. Users of this code are solely responsible for ensuring their activities adhere to legal regulations and obligations.

**No Liability:** The developers of this code assume no liability and shall not be held responsible for any misuse, damage, or harm resulting from the use of this code by unauthorized individuals or malicious actors, whether intentional or accidental. This includes any actions that compromise the security, privacy, integrity, or availability of computer systems and associated resources. In this context, "compromise" refers to the exploitation of known or unknown vulnerabilities within these systems, which may involve circumventing security measures, whether through human actions or electronic means.

**Endorsement for Specific Scenarios:** The use of this code is explicitly endorsed by the developers in particular contexts, such as educational environments and authorized penetration testing engagements. These engagements should have a clearly defined objective: the identification and mitigation of vulnerabilities in systems, with the goal of enhancing their resistance to exploitation and attacks by malicious actors. These objectives should align with the defined threat models relevant to the specific scenario.

By using this code, you acknowledge and accept these terms and conditions. Any use of this code that does not comply with these terms is strictly prohibited.


