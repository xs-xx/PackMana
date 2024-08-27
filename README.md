Tired of installing packagas or failing requirements.txt installs. Well clone and copy and paste this at the top of your code and it will do the rest. 

from PackMana import pack_mana
mana = pack_mana.Pack_Mana()
mana.install_missing_packages()
