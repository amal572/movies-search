(function(e){function t(t){for(var o,n,i=t[0],c=t[1],l=t[2],u=0,d=[];u<i.length;u++)n=i[u],Object.prototype.hasOwnProperty.call(a,n)&&a[n]&&d.push(a[n][0]),a[n]=0;for(o in c)Object.prototype.hasOwnProperty.call(c,o)&&(e[o]=c[o]);f&&f(t);while(d.length)d.shift()();return s.push.apply(s,l||[]),r()}function r(){for(var e,t=0;t<s.length;t++){for(var r=s[t],o=!0,n=1;n<r.length;n++){var i=r[n];0!==a[i]&&(o=!1)}o&&(s.splice(t--,1),e=c(c.s=r[0]))}return e}var o={},n={1:0},a={1:0},s=[];function i(e){return c.p+"js/"+({}[e]||e)+"."+{2:"55232486",3:"e3b7ad2b",4:"8898135f",5:"eae884b3",6:"86264ffd",7:"77a79f4e",8:"3a1c612c",9:"46777481"}[e]+".js"}function c(t){if(o[t])return o[t].exports;var r=o[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,c),r.l=!0,r.exports}c.e=function(e){var t=[],r={2:1,3:1,4:1,5:1};n[e]?t.push(n[e]):0!==n[e]&&r[e]&&t.push(n[e]=new Promise((function(t,r){for(var o="css/"+({}[e]||e)+"."+{2:"c3897fb3",3:"c3897fb3",4:"b1f2e5a8",5:"b1f2e5a8",6:"31d6cfe0",7:"31d6cfe0",8:"31d6cfe0",9:"31d6cfe0"}[e]+".css",a=c.p+o,s=document.getElementsByTagName("link"),i=0;i<s.length;i++){var l=s[i],u=l.getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(u===o||u===a))return t()}var d=document.getElementsByTagName("style");for(i=0;i<d.length;i++){l=d[i],u=l.getAttribute("data-href");if(u===o||u===a)return t()}var f=document.createElement("link");f.rel="stylesheet",f.type="text/css",f.onload=t,f.onerror=function(t){var o=t&&t.target&&t.target.src||a,s=new Error("Loading CSS chunk "+e+" failed.\n("+o+")");s.code="CSS_CHUNK_LOAD_FAILED",s.request=o,delete n[e],f.parentNode.removeChild(f),r(s)},f.href=a;var p=document.getElementsByTagName("head")[0];p.appendChild(f)})).then((function(){n[e]=0})));var o=a[e];if(0!==o)if(o)t.push(o[2]);else{var s=new Promise((function(t,r){o=a[e]=[t,r]}));t.push(o[2]=s);var l,u=document.createElement("script");u.charset="utf-8",u.timeout=120,c.nc&&u.setAttribute("nonce",c.nc),u.src=i(e);var d=new Error;l=function(t){u.onerror=u.onload=null,clearTimeout(f);var r=a[e];if(0!==r){if(r){var o=t&&("load"===t.type?"missing":t.type),n=t&&t.target&&t.target.src;d.message="Loading chunk "+e+" failed.\n("+o+": "+n+")",d.name="ChunkLoadError",d.type=o,d.request=n,r[1](d)}a[e]=void 0}};var f=setTimeout((function(){l({type:"timeout",target:u})}),12e4);u.onerror=u.onload=l,document.head.appendChild(u)}return Promise.all(t)},c.m=e,c.c=o,c.d=function(e,t,r){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(c.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)c.d(r,o,function(t){return e[t]}.bind(null,o));return r},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="",c.oe=function(e){throw console.error(e),e};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],u=l.push.bind(l);l.push=t,l=l.slice();for(var d=0;d<l.length;d++)t(l[d]);var f=u;s.push([0,0]),r()})({0:function(e,t,r){e.exports=r("2f39")},"2f39":function(e,t,r){"use strict";r.r(t);r("e6cf"),r("5319"),r("7d6e"),r("e54f"),r("985d"),r("31cd");var o=r("2b0e"),n=r("1f91"),a=r("42d2"),s=r("b05d"),i=r("2a19");o["a"].use(s["a"],{config:{},lang:n["a"],iconSet:a["a"],plugins:{Notify:i["a"]}});var c=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"q-app"}},[r("router-view")],1)},l=[],u={name:"App"},d=u,f=r("2877"),p=Object(f["a"])(d,c,l,!1,null,null,null),g=p.exports,m=r("ded3"),h=r.n(m),v=r("2f62"),b=r("bc3a"),y=r.n(b),w=e=>{let t=e.response.status,r=e.response.data,o=e.response.config;if(o.disableNotify)return;let n="",a="";400==t?(n=Object.values(r)[0],a="Validation Error"):401==t?(n=Object.values(r)[0],a="Authentication Error"):403==t?(n=Object.values(r)[0],a="Authorization Error"):500==t&&(n="Internal Server Error"),i["a"].create({message:n,caption:a,position:"top-right",type:"negative"})},P=r("b906");const S=y.a.create({baseURL:"https://baraa.usol.ca"});S.interceptors.request.use((e=>{let t=P["a"].getTokens();return t.access&&(e.headers["Authorization"]=`Bearer ${t.access}`),e}),(e=>Promise.reject(e))),S.interceptors.response.use((e=>e),(e=>(w(e),Promise.reject(e)))),o["a"].prototype.$axios=S;const j="user/register/",M="user/login/",O="user/personal_info/",E="director/view/",T="film/create/";class C{static register(e){return S.post(j,e).then((({data:e})=>e))}static login(e){return S.post(M,e).then((({data:e})=>e))}static getUser(){return S.get(O,{disableNotify:!0}).then((({data:e})=>e))}}var k={namespaced:!0,actions:{async register({},e){let t=await C.register(e);return P["a"].saveTokens(t),t}}},L={namespaced:!0,actions:{async login({},e){let t=await C.login(e);return P["a"].saveTokens(t),t}}};class _{static getCategories(){return S.get("/category/view/").then((({data:e})=>e))}}class x{static getDirectors(){return S.get(E).then((({data:e})=>e))}}class A{static addMovie(e){return S.post(T,e).then((({data:e})=>e))}static searchMovies(){return new Promise((e=>{setTimeout((()=>e([1,2,3,4,5,6,7,8,9,10,11,12,13,14])),2e3)}))}static getRecommendedMovies(){return new Promise((e=>{setTimeout((()=>e([1,2,3,4,5,6,7,8,9,10,11,12,13,14])),2e3)}))}}var D={namespaced:!0,state:{categories:[],directors:[]},getters:{categories:e=>e.categories,directors:e=>e.directors},mutations:{setCategories(e,t){e.categories=t},setDirectors(e,t){e.directors=t}},actions:{async fetchData({dispatch:e}){e("getCategories"),e("getDirectors")},async getCategories({commit:e}){let t=await _.getCategories();e("setCategories",t)},async getDirectors({commit:e}){let t=await x.getDirectors();e("setDirectors",t)},async submit({},e){let t=await A.addMovie(e);console.error(t)}}},I={namespaced:!0,state:{loading:!1,movies:[]},getters:{loading:e=>e.loading,movies:e=>e.movies},mutations:{setLoading(e,t){e.loading=t},setMovies(e,t){e.movies=t}},actions:{async fetchMovies({commit:e}){e("setLoading",!0);let t=await A.getRecommendedMovies();e("setMovies",t),e("setLoading",!1)}}},N={namespaced:!0,state:{loading:!1,movies:[]},getters:{loading:e=>e.loading,movies:e=>e.movies},mutations:{setLoading(e,t){e.loading=t},setMovies(e,t){e.movies=t}},actions:{async fetchMovies({commit:e}){e("setLoading",!0);let t=await A.searchMovies();e("setMovies",t),e("setLoading",!1)}}},B={SignUp:k,Login:L,AddMovie:D,Home:I,Search:N};o["a"].use(v["a"]);var U=function(){const e=new v["a"].Store({modules:h()({},B),strict:!1});return e},q=r("8c4f");r("ddb0");const V=[{path:"/",component:()=>Promise.all([r.e(0),r.e(6)]).then(r.bind(null,"713b")),async beforeEnter(e,t,r){C.getUser().then((()=>r())).catch((()=>r("/auth/login")))},children:[{path:"",component:()=>Promise.all([r.e(0),r.e(2)]).then(r.bind(null,"f5b8"))},{path:"movies/add",component:()=>Promise.all([r.e(0),r.e(9)]).then(r.bind(null,"b043"))},{path:"movies/search",component:()=>Promise.all([r.e(0),r.e(3)]).then(r.bind(null,"efe3"))}]},{path:"/auth",component:()=>Promise.all([r.e(0),r.e(7)]).then(r.bind(null,"3ce7")),beforeEnter(e,t,r){C.getUser().then((()=>r("/"))).catch((()=>r()))},children:[{path:"login",component:()=>Promise.all([r.e(0),r.e(4)]).then(r.bind(null,"efcf"))},{path:"sign-up",component:()=>Promise.all([r.e(0),r.e(5)]).then(r.bind(null,"80fd"))}]},{path:"*",component:()=>Promise.all([r.e(0),r.e(8)]).then(r.bind(null,"e51e"))}];var $=V;o["a"].use(q["a"]);var R=function(){const e=new q["a"]({scrollBehavior:()=>({x:0,y:0}),routes:$,mode:"hash",base:""});return e},z=async function(){const e="function"===typeof U?await U({Vue:o["a"]}):U,t="function"===typeof R?await R({Vue:o["a"],store:e}):R;e.$router=t;const r={router:t,store:e,render:e=>e(g),el:"#q-app"};return{app:r,store:e,router:t}},H=r("ff52"),J=r("bc78");H["a"].set(!0),J["a"].setBrand("primary","#9c27b0");var F=async()=>{};const K="";async function Q(){const{app:e,store:t,router:r}=await z();let n=!1;const a=e=>{n=!0;const t=Object(e)===e?r.resolve(e).route.fullPath:e;window.location.href=t},s=window.location.href.replace(window.location.origin,""),i=[void 0,F];for(let l=0;!1===n&&l<i.length;l++)if("function"===typeof i[l])try{await i[l]({app:e,router:r,store:t,Vue:o["a"],ssrContext:null,redirect:a,urlPath:s,publicPath:K})}catch(c){return c&&c.url?void(window.location.href=c.url):void console.error("[Quasar] boot error:",c)}!0!==n&&new o["a"](e)}Q()},"31cd":function(e,t,r){},b906:function(e,t,r){"use strict";r.d(t,"a",(function(){return a}));const o="access",n="refresh";class a{static saveTokens({access:e,refresh:t}){void 0!==e&&localStorage.setItem(o,e),void 0!==e&&localStorage.setItem(n,t)}static getTokens(){return{access:localStorage.getItem(o)||void 0,refresh:localStorage.getItem(n)||void 0}}static resetTokens(){localStorage.removeItem(o),localStorage.removeItem(n)}}}});