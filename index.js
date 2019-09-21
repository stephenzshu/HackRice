const Koa = require('koa');
const Router = require('koa-router');
const logger = require('koa-logger');
const XLSX = require('xlsx');

app = new Koa();
router = new Router();
app.use(logger());

/*router.get("/test", (ctx) => {
  ctx.body = "test";
});*/
const workbook = XLSX.readFile("RiceHackathonFile.xlsx");

router.get("/get-worker-details", (ctx) => {
  ctx.body = XLSX.utils.sheet_to_json(workbook["Sheets"]["Worker Details"]);
});

router.get("/get-equipment-details", (ctx) => {
  ctx.body = XLSX.utils.sheet_to_json(workbook["Sheets"]["Equipment Details"]);
});

router.get("/get-facility-details", (ctx) => {
  ctx.body = XLSX.utils.sheet_to_json(workbook["Sheets"]["Facility Details"]);
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(process.env.PORT || 3000);
