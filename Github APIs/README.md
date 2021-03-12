# Github APIs
[Click Here](https://developer.github.com/v3) to view the documentation.

## Creating token
[Personal Token](https://github.com/settings/tokens) - Navigate to this link.
- Click **Generate new token**.
- Give your token a descriptive name.
- Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select **repo**.
- Click **Generate token**.
- Copy the token.

For further details, view [Github's documentation](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## Storing the token as an ENVIRONMENT VARIABLE
- Open **Command prompt**.
- Type the following: 
```ps
setx GIT_TOKEN your-token
```
## Verifying the ENVIRONMENT VARIABLE
- **Restart** the Command Prompt.
- Type the following:
```ps
echo %GIT_TOKEN%
```
- If it doesn't display your token value, make sure that you restarted your Command Prompt.

## Installing Packages
- Install the following package dependencies using pip:
```ps
pip install requests
```

## Download and run the scripts
Click the link of your choice and press **Ctrl+S** to download the script.
1) [Creating a new repo](https://raw.githubusercontent.com/DhilipSanjay/API-Snippets/master/Github%20APIs/createRepo.py)
2) [View the contents of your repo](https://raw.githubusercontent.com/DhilipSanjay/API-Snippets/master/Github%20APIs/viewContents.py)


Happy coding!
