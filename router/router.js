const Koa = require('koa');
const Router = require('koa-router');
const logger = require('koa-logger');
const bodyParser = require('koa-bodyparser');
const XLSX = require('xlsx');
const { spawn } = require('child_process');
const request = require('superagent');

app = new Koa();
router = new Router();
app.use(logger());
app.use(bodyParser());

/*router.get("/test", (ctx) => {
  ctx.body = "test";
});*/
const workbook = XLSX.readFile(__dirname + "/" + "RiceHackathonFile.xlsx");

router.get("/get-worker-details", (ctx) => {
  ctx.body = XLSX.utils.sheet_to_json(workbook["Sheets"]["Worker Details"]);
});

router.get("/get-equipment-details", (ctx) => {
  ctx.body = XLSX.utils.sheet_to_json(workbook["Sheets"]["Equipment Details"]);
});

router.get("/get-facility-details", (ctx) => {
  ctx.body = XLSX.utils.sheet_to_json(workbook["Sheets"]["Facility Details"]);
});

router.post("/retrieve-work", async (ctx) => {
  // Call python method to retieve initial work orders
  let arg1 = ctx.request.body['name'];
  console.log(arg1);
  const pythonProcess = spawn('python3', ["main.py", "retrieveWork", arg1]);

  pythonProcess.on('exit', (code) => {
    console.log("EXITED " + code);
  });

  const json = await new Promise((resolve, reject) => {
    pythonProcess.stdout.on('data', (data) => {
      console.log('test');
      let temp = data.toString('utf8').split(" ");
      retrieved_work_json = {
        "workID": temp[0],
        "facility": temp[1],
        "equipment": temp[2],
        "equipmentID": temp[3],
        "priority": temp[4],
        "time": temp[5],
        "submissionTime": temp[6],
        "inProgress": temp[7]
      }
      resolve(retrieved_work_json);
    });
  });
  console.log("bing");
  ctx.body = json;
});

router.post("/get-new-work-order", async (ctx) => {
  // Calls python method to retrieve a new work order
  let arg1 = ctx.request.body['name'];
  console.log(arg1);
  const pythonProcess = spawn('python3', ["main.py", "getNewWork", arg1]);

  pythonProcess.on('exit', (code) => {
    console.log("EXITED " + code);
  });

  const json = await new Promise((resolve, reject) => {
    pythonProcess.stdout.on('data', (data) => {
      let temp = data.toString('utf8').split(" ");
      retrieved_work_json = {
        "workID": temp[0],
        "facility": temp[1],
        "equipment": temp[2],
        "equipmentID": temp[3],
        "priority": temp[4],
        "time": temp[5],
        "submissionTime": temp[6],
        "inProgress": temp[7]
      }
      resolve(retrieved_work_json);
    });
  });

  ctx.body = json;
});

router.post("/stop-work", async (ctx) => {
  // Call python method that finishes work order for worker
  let arg1 = ctx.request.body['name'];
  let arg2 = ctx.request.body['time'];
  const pythonProcess = spawn('python', ["./main.py", "stopWork", arg1, arg2]);

  pythonProcess.on('exit', (code) => {
    console.log("EXITED " + code);
  });
  
  const result = await new Promise((resolve, reject) => {
    pythonProcess.stdout.on('data', (data) => {
      let temp = data.toString('utf8');
      if (temp == "Success") resolve()
      else reject()
    });
  });

  ctx.body = "Work task ended.";
});

// Test routes
router.get("/get-test", (ctx) => {
  request.get("https://morning-headland-65470.herokuapp.com/get-worker-details")
    .set('Accept', 'application/json')
    .then(res => {
      console.log(res);
    });
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(process.env.PORT || 3000);
