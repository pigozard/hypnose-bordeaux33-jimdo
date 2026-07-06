/*  Typo
----------------------------------------------- */

a:link, a:visited
{
    text-decoration: underline;
    color:#EC4413;
}
a:active { 	text-decoration: underline; }
a:hover { text-decoration:none; }


h1 { font:bold 18px/140% "Trebuchet MS", Verdana, sans-serif; }
h2 { font:bold 14px/140% "Trebuchet MS", Verdana, sans-serif; }

p {	font: 11px/140% Verdana, Geneva, Arial, Helvetica, sans-serif;}

/*  Layout
----------------------------------------------- */

body {
    background: #333333 url(bg.gif) no-repeat top left;
    padding:35px 0 0 0;
    margin:0;
    font: 11px/140% Verdana, Geneva, Arial, Helvetica, sans-serif;
}

#container
{
    margin:0 auto;
    width:834px;
    background:white;
}

#header
{
    padding:17px;
}

#header h1,
#header a
{
    padding:0;
    font-family:"Helvetica","Lucida Sans Unicode",Tahoma,Verdana,Arial,Helvetica,sans-serif;
    font-size:30px;
    font-weight:normal;
    text-decoration:none;
    line-height:1.3em;
    color:#666666;
    text-align:right;
}

#header a:hover { text-decoration:none;  }


#navigation
{
    float:left;
    width:220px;
    padding:17px;

}
#sidebar
{
    padding-top:10px;
}

#content
{
    float:right;

    width:530px;
    padding:17px;

}

#footer
{
    clear:both;
    margin-top:10px;
    background:url(footer-bg.gif) repeat-x top;
    height:65px;
}

#footer .gutter
{
    height:30px;
    padding:35px 15px 0 90px;
}

/*  Navigation
----------------------------------------------- */

ul.mainNav1,
ul.mainNav2
{
    margin:0;
    padding: 0;
}


ul.mainNav1 li,
ul.mainNav2 li
{
    display: inline;
    margin: 0;
    padding: 0;
}


ul.mainNav1 li a,
ul.mainNav2 li a
{
    font:normal 11px/140% Verdana, Geneva, Arial, Helvetica, sans-serif;
    text-decoration: none;
    display: block;
    color:#333;
    border-bottom:1px solid #CCC;
}


ul.mainNav1 li a { padding:4px 4px 4px 4px; }
ul.mainNav2 li a { padding:4px 4px 4px 14px; }
ul.mainNav3 li a { padding:4px 4px 4px 24px; }


ul.mainNav1 a:hover
{
    background:#EEE;
    color:black;
}

ul.mainNav1 a.current { font-weight:bold; }
