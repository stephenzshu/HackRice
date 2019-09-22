const Koa = require('koa');
const Router = require('koa-router');
const logger = require('koa-logger');
const XLSX = require('xlsx');
const spawn = require('child_process');
const request = require('superagent');

app = new Koa();
router = new Router();
app.use(logger());

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

// Test
router.get("/meta-test", (ctx) => {
  request.get("https://morning-headland-65470.herokuapp.com/get-worker-details")
    .set('Accept', 'application/json')
    .then(res => {
      console.log(res);
    });
});

router.post("/get-new-work-order", workerName, (ctx) => {
  // arg1 will be function to call, arg2 ... will be parameters for function call
  let json;
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
  ctx.body = json;
});

router.get("/finish-current-work-order", (ctx) => {
  // Call python method that finishes work order for worker
  const pythonProcess = spawn.spawn('python', ["./main.py", arg1, arg2]);
  pythonProcess.stdout.on('data', (data) => {
    ctx.status = 200;
    ctx.body = "Current work order successfully removed";
  });
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(process.env.PORT || 3000);
