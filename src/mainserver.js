const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req,res) => {
    res.send("Server is alive and running");
});

let ID = [
    {
        "satID": 47761
    }
]

app.get('/api/SatID', (req,res) => {
    res.send("39088");
});

/*
In progress, allows user to respond to server with a satellite ID for analysis.

app.put('/api/SatID', (req,res) => {
    let newID = {
        "satID": req.body.satID
    };
ID.push(newID);
console.log(ID);
res.send(ID);
});

app.delete('/api/SatID', (req,res) => {
    const SatID = req.params.SatID;
    const api = SatID

    delete SatID;

    res.send("Data Cleared");
});
*/

app.get('/api/tle', (req, res) => {
    const spawn = require("child_process").spawn;

    const pythonProcess = spawn('python',["spacetrackCALL.py"]);
    pythonProcess.stdout.on('data', (data) => {

        mystr = data.toString();
        console.log(`Data To String ${mystr} Type of ${typeof mystr}`);

        myjson = JSON.parse(mystr);
        console.log(`JSON IS : ${myjson}`);

    });
res.json(myjson)
});

app.get('/api/grndtrk', (req, res) => {
    const spawn = require("child_process").spawn;

    const pythonProcess = spawn('python',["simulation.py"]);
    pythonProcess.stdout.on('data', (data) => {

        mystr = data.toString();
        console.log(`Data To String ${mystr} Type of ${typeof mystr}`);

        myjson = JSON.parse(mystr);
        console.log(`JSON IS : ${myjson}`);
    });
res.json(myjson)
});

const port = process.env.PORT || (3000);
app.listen(port, () => console.log('Listening on port: ' + port));
