# Github APIs
[Click Here](https://developer.github.com/v3) to view the documentation.

## Creating token
[Personal Token](https://github.com/settings/tokens) - Navigate to this link
- Click *Generate new token*
- Give your token a descriptive name.
- Select the scopes, or permissions, you'd like to grant this token. To use your token to access repositories from the command line, select **repo**.
- Click **Generate token**.
- Copy the token.

For further details, view [Github's documentation](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

## Storing the token as an ENVIRONMENT VARIABLE
Open **Command prompt**
- Type the following: 

  **setx GIT_TOKEN** _your-token_

## Verifying the ENVIRONMENT VARIABLE
- Restart the Command Prompt
- Type the following:

  **echo %GIT_TOKEN%**
- If it doesn't display your token value, make sure your restarted your Command Prompt


### Now download and run any of the scripts you want !!
