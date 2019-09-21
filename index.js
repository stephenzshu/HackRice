const Koa = require('koa');
const Router = require('koa-router');

app = new Koa();
router = new Router();

router.get("/test", (ctx) => {
  ctx.body = "test";
});

app.use(router.routes());
app.use(router.allowedMethods());

app.listen(process.env.PORT || 3000);
