const Koa = require('koa');
const Router = require('koa-router');
const logger = require('koa-logger');
const bodyParser = require('koa-bodyparser');
const XLSX = require('xlsx');
const spawn = require('child_process');
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

router.get("/post-test", (ctx) => {
  request.post("https://morning-headland-65470.herokuapp.com/get-new-work-order")
    .send('test')
    .catch(err => {
      console.log(err);
    })
});

router.post("/get-new-work-order", bodyParser, (ctx) => {
  // arg1 will be function to call, arg2 ... will be parameters for function call
  console.log("yes");
  let test = ctx.request.body;
  ctx.body = test;
  /*let json;
  let arg1 = workerName;
  const pythonProcess = spawn.spawn('python', ["./main.py", "retrieveWork", arg1]);
  pythonProcess.stdout.on('data', (data) => {
    json = {
      "workID": null,
      "facility": null,
      "equipment": null,
      "equipmentID": null,
      "priority": null,
      "time": null,
      "submissionTime": null,
      "inProgress": null
    }
  });
  ctx.body = json;*/
});

router.get("/finish-current-work-order", (ctx) => {
  // Call python method that finishes work order for worker
  const pythonProcess = spawn.spawn('python', ["./main.py", arg1, arg2]);
  pythonProcess.stdout.on('data', (data) => {
    ctx.status = 200;
    ctx.body = "Current work order successfully removed";
  });
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
