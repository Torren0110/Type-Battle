# Type-Battle
Web Application where you can hone your typing skill, get your typing stats and compete with other battlers.

# Dependencies
<ul>
  <li>Python                       3.10.2</li>
  <li>pip                          22.3.1</li>
  <li>Django                       4.1.7</li>
  <li>django-crispy-forms          2.0</li>
  <li>django-guest-user            0.5.4</li>
  <li>crispy-bootstrap4            2022.1</li>
</ul>

# How To Run

<ol>
  <li>
    Check if you have python installed or not.
      <ul>
        <li>To check if you have python or not run command: python</li>
        <li>Install python from https://www.python.org/downloads/ if it is not installed.</li>
      </ul>
  </li>
  <li>
    Check if you have the required packages.
      <ul>
          <li>To install a python package run command : pip install package_name</li>
          <li>If the package is already installed the above command will return requirement already fullfilled</li>
      </ul>
  </li>
  <li>
    Open the typeRacer folder in command prompt,where there will be a manage.py file.
  </li>
  <li>
    To Start The server:
      <ul>
        <li>Run command : python manage.py runserver</li>
        <li>Go to the url given after running the above command</li>
      </ul>
  </li>
  <li>
    To Add a Passage to the database:
      <ul>
        <li>Log in as a super user</li>
        <li>The option to add a passage will be available if you login as the super user</li>
      </ul>
  </li>
  <li>
    To Create a super user:
      <ul>
        <li>Open the typeRacer folder in command prompt, there will be a manage.py file.</li>
        <li>Run the Command: python manage.py createsuperuser</li>
        <li>After running the command enter the details asked in the prompt</li>
        <li>Note that when you enter your password, your password will not be shown in the command prompt.</li>
      </ul>
  </li>
</ol>
