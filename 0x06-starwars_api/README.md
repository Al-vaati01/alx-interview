# 0x06. Star Wars API
```Algorithm```
```API```
```JavaScript```

### Star Wars Characters Script

This script retrieves and prints the list of characters from a specified Star Wars movie using the Star Wars API. It takes the Movie ID as a positional argument and displays the character names one per line in the same order as they appear in the "characters" list in the /films/ endpoint.

#### Prerequisites
Before you can run the script, ensure you have Node.js installed on your system.

#### Installation
Clone the repository or download the script file.

Install the required request module using npm:


```
$ npm install request
```

**Usage**
To run the script, use the following command:


```
$ node 0-starwars_characters.js <Movie ID>
```
Replace `<Movie ID>` with the ID of the Star Wars movie you want to retrieve characters from.

*For example:*

```
$ node 0-starwars_characters.js 3
```
This command will print the list of characters from "Return of the Jedi" (Movie ID 3) to the console, one character name per line.

**Script Explanation**

The script makes an HTTP request to the Star Wars API to retrieve information about the specified movie. It then checks if the response contains a "characters" property. If it does, the script iterates through the list of character URLs, makes individual requests for each character, and prints their names to the console.

If any errors occur during the requests, the script will display an error message.

If the "characters" property is not found in the response, it will indicate that in the console.

**Example Output**

Here's an example of what the script's output might look like:

```
$ node 0-starwars_characters.js 3
Obi-Wan Kenobi
Palpatine
Darth Vader
R2-D2
Jabba Desilijic Tiure
Boba Fett
Lando Calrissian
Nien Nunb
Leia Organa
Luke Skywalker
Chewbacca
Bib Fortuna
C-3PO
Han Solo
Wedge Antilles
Arvel Crynyd
Mon Mothma
Wicket Systri Warrick
Yoda
Ackbar
```
This output corresponds to the characters from "Return of the Jedi" (Movie ID 3).


