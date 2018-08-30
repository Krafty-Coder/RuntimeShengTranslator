#	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	*        RUNTIME SHENG TRANSLATOR -  REVERSE DIRECTION   *
#	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	*  Welcome to Runtime Sheng translator. v1.0.0           *
#	*  MIT License, Copyright(c) 2018, Antony Muga           *
#	*  All Rights Reserved.                                  *
#	*  Author: Antony Muga                                   *
#	----------------------------------------------------------
#	*  Project's Links:                                      *
#	*  Twitter: https://twitter.com/RuntimeLab               *
#	*  Runtime Lab on LinkedIn                               *
#	*  RuntimeLab on Github                                  *
#	*  RuntimeShengTranslator project on GitHub              *
#	----------------------------------------------------------
#	*  Personal social links:                                *
#	*  GitHub: https://github.com/antonymuga/                *
#	*  Website: https://antonymuga.github.io                 *
#	*  LinkedIn: https://www.linkedin.com/in/antony-muga/    *
#	*  Email: https://sites.google.com/view/antonymuga/home  *
#	----------------------------------------------------------
# The below 'import sys' is currently vestigial now but will come in handy while writing new submissions
# into the individual dictionary files, open, write, close and all that Jazz
import sys

# Used for finding the nearest matches
from difflib import get_close_matches, SequenceMatcher

# Import the project details
import about

# Import the dictionaries for the different languages
from Dictionaries import ToEng # English dictionary
from Dictionaries import ToFre # French dictionary
from Dictionaries import ToGer # German dictionary
from Dictionaries import ToSpa # Spanish dictionary
from Dictionaries import ToIta # Italian dictionary

# Print line separator
print("\n","*"*75, "\n")

# Print the project details
print(about.projectDetails)

# Print line separator for different sections
print("\n","*"*75, "\n")


# Declare a tuple that contains all the imported dictionaries
dictionaryList = (ToEng.shengToEng, ToFre.shengToFre, ToGer.shengToGer, ToSpa.shengToSpa, ToIta.shengToIta)

# Enter new word submissions
submissions = []