(function(e){function t(t){for(var a,o,i=t[0],c=t[1],l=t[2],u=0,d=[];u<i.length;u++)o=i[u],Object.prototype.hasOwnProperty.call(n,o)&&n[o]&&d.push(n[o][0]),n[o]=0;for(a in c)Object.prototype.hasOwnProperty.call(c,a)&&(e[a]=c[a]);g&&g(t);while(d.length)d.shift()();return s.push.apply(s,l||[]),r()}function r(){for(var e,t=0;t<s.length;t++){for(var r=s[t],a=!0,o=1;o<r.length;o++){var i=r[o];0!==n[i]&&(a=!1)}a&&(s.splice(t--,1),e=c(c.s=r[0]))}return e}var a={},o={1:0},n={1:0},s=[];function i(e){return c.p+"js/"+({}[e]||e)+"."+{2:"4bf704ce",3:"5a505317",4:"8898135f",5:"eae884b3",6:"019e5a74",7:"77a79f4e",8:"3a1c612c",9:"46777481"}[e]+".js"}function c(t){if(a[t])return a[t].exports;var r=a[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,c),r.l=!0,r.exports}c.e=function(e){var t=[],r={2:1,3:1,4:1,5:1};o[e]?t.push(o[e]):0!==o[e]&&r[e]&&t.push(o[e]=new Promise((function(t,r){for(var a="css/"+({}[e]||e)+"."+{2:"1324565b",3:"e2bd9b66",4:"b1f2e5a8",5:"b1f2e5a8",6:"31d6cfe0",7:"31d6cfe0",8:"31d6cfe0",9:"31d6cfe0"}[e]+".css",n=c.p+a,s=document.getElementsByTagName("link"),i=0;i<s.length;i++){var l=s[i],u=l.getAttribute("data-href")||l.getAttribute("href");if("stylesheet"===l.rel&&(u===a||u===n))return t()}var d=document.getElementsByTagName("style");for(i=0;i<d.length;i++){l=d[i],u=l.getAttribute("data-href");if(u===a||u===n)return t()}var g=document.createElement("link");g.rel="stylesheet",g.type="text/css",g.onload=t,g.onerror=function(t){var a=t&&t.target&&t.target.src||n,s=new Error("Loading CSS chunk "+e+" failed.\n("+a+")");s.code="CSS_CHUNK_LOAD_FAILED",s.request=a,delete o[e],g.parentNode.removeChild(g),r(s)},g.href=n;var f=document.getElementsByTagName("head")[0];f.appendChild(g)})).then((function(){o[e]=0})));var a=n[e];if(0!==a)if(a)t.push(a[2]);else{var s=new Promise((function(t,r){a=n[e]=[t,r]}));t.push(a[2]=s);var l,u=document.createElement("script");u.charset="utf-8",u.timeout=120,c.nc&&u.setAttribute("nonce",c.nc),u.src=i(e);var d=new Error;l=function(t){u.onerror=u.onload=null,clearTimeout(g);var r=n[e];if(0!==r){if(r){var a=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;d.message="Loading chunk "+e+" failed.\n("+a+": "+o+")",d.name="ChunkLoadError",d.type=a,d.request=o,r[1](d)}n[e]=void 0}};var g=setTimeout((function(){l({type:"timeout",target:u})}),12e4);u.onerror=u.onload=l,document.head.appendChild(u)}return Promise.all(t)},c.m=e,c.c=a,c.d=function(e,t,r){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(c.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)c.d(r,a,function(t){return e[t]}.bind(null,a));return r},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="",c.oe=function(e){throw console.error(e),e};var l=window["webpackJsonp"]=window["webpackJsonp"]||[],u=l.push.bind(l);l.push=t,l=l.slice();for(var d=0;d<l.length;d++)t(l[d]);var g=u;s.push([0,0]),r()})({0:function(e,t,r){e.exports=r("2f39")},"2f39":function(e,t,r){"use strict";r.r(t);r("e6cf"),r("5319"),r("7d6e"),r("e54f"),r("985d"),r("31cd");var a=r("2b0e"),o=r("1f91"),n=r("42d2"),s=r("b05d"),i=r("2a19");a["a"].use(s["a"],{config:{},lang:o["a"],iconSet:n["a"],plugins:{Notify:i["a"]}});var c=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"q-app"}},[r("router-view")],1)},l=[],u={name:"App"},d=u,g=r("2877"),f=Object(g["a"])(d,c,l,!1,null,null,null),p=f.exports,h=r("ded3"),m=r.n(h),v=r("2f62"),b=r("bc3a"),y=r.n(b),w=e=>{let t=e.response.status,r=e.response.data,a=e.response.config;if(a.disableNotify)return;let o="",n="";400==t?(o=Object.values(r)[0],n="Validation Error"):401==t?(o=Object.values(r)[0],n="Authentication Error"):403==t?(o=Object.values(r)[0],n="Authorization Error"):500==t&&(o="Internal Server Error"),i["a"].create({message:o,caption:n,position:"top-right",type:"negative"})},P=r("b906");const C=y.a.create({baseURL:"http://hallogen.insoftonline.de"});C.interceptors.request.use((e=>{let t=P["a"].getTokens();return t.access&&(e.headers["Authorization"]=`Bearer ${t.access}`),e}),(e=>Promise.reject(e))),C.interceptors.response.use((e=>e),(e=>(w(e),Promise.reject(e)))),a["a"].prototype.$axios=C;var S=async({store:e})=>{e.dispatch("Categories/fetchCategories")};const M="user/register/",L="user/login/",j="user/personal_info/",O="director/view/",E="film/create/",k="dsearch/SBert/",T="Recomender/view/",_="review/create/";class x{static register(e){return C.post(M,e).then((({data:e})=>e))}static login(e){return C.post(L,e).then((({data:e})=>e))}static getUser(){return C.get(j,{disableNotify:!0}).then((({data:e})=>e))}}var A={namespaced:!0,actions:{async register({},e){let t=await x.register(e);return P["a"].saveTokens(t),t}}},D={namespaced:!0,actions:{async login({},e){let t=await x.login(e);return P["a"].saveTokens(t),t}}};class I{static getCategories(){return C.get("/category/view/").then((({data:e})=>e))}}class B{static getDirectors(){return C.get(O).then((({data:e})=>e))}}class N{static addMovie(e){return C.post(E,e).then((({data:e})=>e))}static searchMovies(e){return C.post(k,e).then((({data:e})=>e))}static getRecommendedMovies(){return C.post(T).then((({data:e})=>e))}}var U={namespaced:!0,state:{categories:[],directors:[]},getters:{categories:e=>e.categories,directors:e=>e.directors},mutations:{setCategories(e,t){e.categories=t},setDirectors(e,t){e.directors=t}},actions:{async fetchData({dispatch:e}){e("getCategories"),e("getDirectors")},async getCategories({commit:e}){let t=await I.getCategories();e("setCategories",t)},async getDirectors({commit:e}){let t=await B.getDirectors();e("setDirectors",t)},async submit({},e){let t=await N.addMovie(e);console.error(t)}}},q={namespaced:!0,state:{loading:!1,movies:[]},getters:{loading:e=>e.loading,movies:e=>e.movies},mutations:{setLoading(e,t){e.loading=t},setMovies(e,t){e.movies=t}},actions:{async fetchMovies({commit:e}){e("setLoading",!0);let t=await N.getRecommendedMovies();e("setMovies",t),e("setLoading",!1)}}},R={namespaced:!0,state:{loading:!1,movies:[]},getters:{loading:e=>e.loading,movies:e=>e.movies},mutations:{setLoading(e,t){e.loading=t},setMovies(e,t){e.movies=t}},actions:{async fetchMovies({commit:e},t){e("setLoading",!0);let r=await N.searchMovies({search:t});e("setMovies",r),e("setLoading",!1)}}},V={namespaced:!0,state:{loading:!1,categories:[]},getters:{loading:e=>e.loading,categories:e=>e.categories,categoriesByIds:e=>t=>e.categories.filter((e=>t.includes(e.id)))},mutations:{setLoading(e,t){e.loading=t},setCategories(e,t){e.categories=t}},actions:{async fetchCategories({commit:e}){e("setLoading",!0);let t=await I.getCategories();e("setCategories",t),e("setLoading",!1)}}};class ${static reviewMovie(e){return C.post(_,e).then((({data:e})=>e))}}var z={namespaced:!0,state:{loading:!1},getters:{loading:e=>e.loading},mutations:{setLoading(e,t){e.loading=t}},actions:{async rateMovie({commit:e},t){e("setLoading",!0),await $.reviewMovie(t),e("setLoading",!1)}}},H={SignUp:A,Login:D,AddMovie:U,Home:q,Search:R,Categories:V,Reviews:z};a["a"].use(v["a"]);var J=function(){const e=new v["a"].Store({modules:m()({},H),strict:!1});return e},F=r("8c4f");r("ddb0");const K=[{path:"/",component:()=>Promise.all([r.e(0),r.e(6)]).then(r.bind(null,"713b")),async beforeEnter(e,t,r){x.getUser().then((()=>r())).catch((()=>r("/auth/login")))},children:[{path:"",component:()=>Promise.all([r.e(0),r.e(2)]).then(r.bind(null,"f5b8"))},{path:"movies/add",component:()=>Promise.all([r.e(0),r.e(9)]).then(r.bind(null,"b043"))},{path:"movies/search",component:()=>Promise.all([r.e(0),r.e(3)]).then(r.bind(null,"efe3"))}]},{path:"/auth",component:()=>Promise.all([r.e(0),r.e(7)]).then(r.bind(null,"3ce7")),beforeEnter(e,t,r){x.getUser().then((()=>r("/"))).catch((()=>r()))},children:[{path:"login",component:()=>Promise.all([r.e(0),r.e(4)]).then(r.bind(null,"efcf"))},{path:"sign-up",component:()=>Promise.all([r.e(0),r.e(5)]).then(r.bind(null,"80fd"))}]},{path:"*",component:()=>Promise.all([r.e(0),r.e(8)]).then(r.bind(null,"e51e"))}];var Q=K;a["a"].use(F["a"]);var G=function(){const e=new F["a"]({scrollBehavior:()=>({x:0,y:0}),routes:Q,mode:"hash",base:""});return e},W=async function(){const e="function"===typeof J?await J({Vue:a["a"]}):J,t="function"===typeof G?await G({Vue:a["a"],store:e}):G;e.$router=t;const r={router:t,store:e,render:e=>e(p),el:"#q-app"};return{app:r,store:e,router:t}},X=r("ff52"),Y=r("bc78");X["a"].set(!0),Y["a"].setBrand("primary","#9c27b0");var Z=async()=>{};const ee="";async function te(){const{app:e,store:t,router:r}=await W();let o=!1;const n=e=>{o=!0;const t=Object(e)===e?r.resolve(e).route.fullPath:e;window.location.href=t},s=window.location.href.replace(window.location.origin,""),i=[S,Z];for(let l=0;!1===o&&l<i.length;l++)if("function"===typeof i[l])try{await i[l]({app:e,router:r,store:t,Vue:a["a"],ssrContext:null,redirect:n,urlPath:s,publicPath:ee})}catch(c){return c&&c.url?void(window.location.href=c.url):void console.error("[Quasar] boot error:",c)}!0!==o&&new a["a"](e)}te()},"31cd":function(e,t,r){},b906:function(e,t,r){"use strict";r.d(t,"a",(function(){return n}));const a="access",o="refresh";class n{static saveTokens({access:e,refresh:t}){void 0!==e&&localStorage.setItem(a,e),void 0!==e&&localStorage.setItem(o,t)}static getTokens(){return{access:localStorage.getItem(a)||void 0,refresh:localStorage.getItem(o)||void 0}}static resetTokens(){localStorage.removeItem(a),localStorage.removeItem(o)}}}});