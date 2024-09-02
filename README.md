<font color = "blue"><H1>Automatic Package Installer</H1></font>
Tired of installing packagas or failing requirements.txt installs. Well clone and copy and paste this at the top of your code and it will do the rest.

    git clone https://github.com/xs-xx/PackMana.git
<br>
Add this to the top of the code before all other imports. 

    from PackMana import pack_mana
    mana = pack_mana.Pack_Mana()
    mana.install_missing_packages()
