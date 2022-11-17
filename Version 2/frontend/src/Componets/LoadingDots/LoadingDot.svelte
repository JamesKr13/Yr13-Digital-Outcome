
<div class="loader">
  <span style="background:#97D700;"></span>
  <span style="background:#147BD1;"></span>
  <span style="background:#464E7E;"></span>
  <span style="background:#2DCCD3;"></span>
</div>
<style>
  .loader {
    text-align: center;
}
.loader span {
    display: hidden;
    vertical-align: middle;
    width: 24px;
    height: 24px;
    margin: 50px auto;
    border-radius: 50px;
    -webkit-animation: loader 0.9s infinite alternate;
}
.loader span:nth-of-type(2) {
    -webkit-animation-delay: 0.2s;
}
.loader span:nth-of-type(3) {
    -webkit-animation-delay: 0.4s;
}
.loader span:nth-of-type(4) {
    -webkit-animation-delay: 0.6s;
}
@-webkit-keyframes loader {
  0% {
    width: 24px;
    height: 24px;
    opacity: 1;
  }
  100% {
    width: 24px;
    height: 24px;
    opacity: 0.3;
  }
}
</style>