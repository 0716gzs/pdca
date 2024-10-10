<template>
  <div class="footer">
    <div class="footer-content">
      <div class="report-wrap">
        <a href="http://www.beian.gov.cn/portal/registerSystemInfo" class="report-link" target="_blank" rel="noreferrer">
          <img src="https://beian.mps.gov.cn/img/logo01.dd7ff50e.png" alt="" class="report-img">
          <span class="report-link-text">豫公网安备41078402000050号</span>
        </a>

        <div class="report-wrap">
          <a href="https://beian.miit.gov.cn/" class="report-link" target="_blank" rel="noreferrer">
            <span class="report-link-text">豫ICP备2024084793号</span>
          </a>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>
.footer {
  background: rgb(245, 245, 246);
  padding-top: 3px;
  border-top: 1px solid rgb(207, 208, 209);
}

.footer-content {
  display: flex;
  justify-content: center;
}

.report-wrap {
  display: flex;
  align-items: center;
  margin-left: 30px;
}

.report-link {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.report-img {
  height: 20px;
  margin-right: 12px;
}

.report-link-text {
  font-size: 12px;
  line-height: 20px;
  color: rgb(147, 147, 147);
}
</style>
