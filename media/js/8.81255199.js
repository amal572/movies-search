(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[8],{b043:function(e,t,o){"use strict";o.r(t);var r=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{staticClass:"q-pa-xl flex justify-center"},[o("q-card",{staticStyle:{width:"600px"}},[o("q-card-section",[o("div",{staticClass:"text-h6"},[e._v("Add Movie")])]),o("q-card-section",[o("q-form",{on:{submit:function(t){return e.submit(e.form)}}},[o("div",[o("q-input",{attrs:{dense:"",outlined:"",label:"Title",rules:[function(e){return!!e||"Required"}]},model:{value:e.form.title,callback:function(t){e.$set(e.form,"title",t)},expression:"form.title"}})],1),o("div",[o("q-input",{attrs:{dense:"",outlined:"",label:"Production Company",rules:[function(e){return!!e||"Required"}]},model:{value:e.form.production_company,callback:function(t){e.$set(e.form,"production_company",t)},expression:"form.production_company"}})],1),o("div",[o("q-input",{attrs:{dense:"",outlined:"",label:"Description",rules:[function(e){return!!e||"Required"}]},model:{value:e.form.description,callback:function(t){e.$set(e.form,"description",t)},expression:"form.description"}})],1),o("div",[o("q-input",{attrs:{dense:"",outlined:"",rules:[""]},scopedSlots:e._u([{key:"append",fn:function(){return[o("q-icon",{staticClass:"cursor-pointer",attrs:{name:"event"}},[o("q-popup-proxy",{ref:"qDateProxy",attrs:{"transition-show":"scale","transition-hide":"scale"}},[o("q-date",{attrs:{mask:"YYYY-MM-DD"},model:{value:e.form.release_date,callback:function(t){e.$set(e.form,"release_date",t)},expression:"form.release_date"}},[o("div",{staticClass:"row items-center justify-end"},[o("q-btn",{directives:[{name:"close-popup",rawName:"v-close-popup"}],attrs:{label:"Close",color:"primary",flat:""}})],1)])],1)],1)]},proxy:!0}]),model:{value:e.form.release_date,callback:function(t){e.$set(e.form,"release_date",t)},expression:"form.release_date"}})],1),o("div",[o("q-select",{attrs:{options:e.languages,dense:"",outlined:"",label:"Spoken Language","map-options":"","emit-value":"",rules:[function(e){return!!e||"Required"}]},model:{value:e.form.spoken_language,callback:function(t){e.$set(e.form,"spoken_language",t)},expression:"form.spoken_language"}})],1),o("div",[o("q-input",{attrs:{type:"number",dense:"",outlined:"",label:"Run Time",rules:[function(e){return!!e||"Required"}]},model:{value:e.form.run_time,callback:function(t){e.$set(e.form,"run_time",t)},expression:"form.run_time"}})],1),o("div",[o("q-select",{attrs:{options:e.directors,dense:"",outlined:"",label:"Director",rules:[function(e){return!!e||"Required"}],"option-label":"name","option-value":"id","emit-value":"","map-options":""},model:{value:e.form.director,callback:function(t){e.$set(e.form,"director",t)},expression:"form.director"}})],1),o("div",[o("q-input",{attrs:{dense:"",outlined:"",label:"Link of Film",rules:[function(e){return!!e||"Required"}]},model:{value:e.form.link_of_film,callback:function(t){e.$set(e.form,"link_of_film",t)},expression:"form.link_of_film"}})],1),o("div",[o("q-select",{attrs:{options:e.categories,dense:"",outlined:"",label:"Category",rules:[function(e){return!!e||"Required"}],"option-label":"name","option-value":"id","emit-value":"","map-options":""},model:{value:e.form.categorie,callback:function(t){e.$set(e.form,"categorie",t)},expression:"form.categorie"}})],1),o("div",[o("div",{staticClass:"flex"},[o("div",{staticClass:"text-subtitle1 q-px-sm"},[e._v("Rate")]),o("q-rating",{attrs:{size:"2em",color:"orange",icon:"star_border","icon-selected":"star"},model:{value:e.form.rate,callback:function(t){e.$set(e.form,"rate",t)},expression:"form.rate"}})],1)]),o("div",{staticClass:"flex justify-end q-pt-md"},[o("q-btn",{attrs:{color:"primary",label:"Save",type:"submit"}})],1)])],1)],1)],1)},a=[],i=o("ded3"),n=o.n(i),l=o("2f62");let s=[{label:"English",value:"english"},{label:"Arabic",value:"arabic"}];var c={data:()=>({languages:s,form:{title:"film10",production_company:"new name",description:"this film is",release_date:"2021-05-16",spoken_language:"english",run_time:150,director:2,rate:50,link_of_film:"rr",categorie:1}}),computed:n()({},Object(l["c"])("AddMovie",["categories","directors"])),created(){this.fetchData()},methods:n()({},Object(l["b"])("AddMovie",["fetchData","submit"]))},u=c,d=o("2877"),m=o("f09f"),f=o("a370"),p=o("0378"),v=o("27f9"),b=o("0016"),_=o("7cbe"),q=o("52ee"),g=o("9c40"),k=o("ddd8"),x=o("daf4"),y=o("7f67"),h=o("eebe"),C=o.n(h),$=Object(d["a"])(u,r,a,!1,null,null,null);t["default"]=$.exports;C()($,"components",{QCard:m["a"],QCardSection:f["a"],QForm:p["a"],QInput:v["a"],QIcon:b["a"],QPopupProxy:_["a"],QDate:q["a"],QBtn:g["a"],QSelect:k["a"],QRating:x["a"]}),C()($,"directives",{ClosePopup:y["a"]})}}]);