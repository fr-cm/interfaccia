
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interfaccia</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- CSS  -->
    <style>
        /* Reset globale */
*,
*::before,
*::after {
    box-sizing: border-box;
}

html, body {
    overflow-x: hidden;
}

/* Stili generali per tutti i dispositivi */
h2 {
    text-align: center;
    margin-top: 2rem;
    margin-left: 2rem;
    margin-right: 2rem;
}


.page{
    padding-top: 5rem;
    padding-bottom: 3rem;
}


.table-scrollable {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    width: 100%;
}

/* Stili pulsanti */
.content-row button {
    display: block;
    margin: 1rem auto 0;
    padding: 0.5rem 1rem;
    background-color: #273898;
    color: #fff;
    border: none;
    border-radius: 0.25rem;
    cursor: pointer;
}

.content-row button:hover {
    background-color: #4f72b5e0;
}

.content-row button:active {
    background-color: #0b5ed7;
}

.img1 {
  display: flex;
  margin: 0 auto;
  max-width: 60rem;
  text-align: center;
  justify-content: center;
}
.img2 {
  display: flex;
  margin: 0 auto;
  max-width: 35rem;
  text-align: center;
  justify-content: center;
  padding-right: 1rem;
}

/* ####################### NAVBAR ############################# */
.navbar {
    font-family: 'Gotham', sans-serif;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
}

/* Navbar desktop */
@media (min-width: 769px) {
    .navbar-nav .nav-link,
    .navbar-brand {
        font-weight: bold;
    }

    .navbar-brand {
        font-size: 24px;
        line-height: 1;
        display: block;
        margin-bottom: 0;
    }

    .text-muted {
        font-size: 14px;
        font-style: italic;
        line-height: 0.3;
        display: block;
        margin-top: 0.1rem;
        color: #8ca5d4;
    }

    .dropdown-menu {
        border-radius: 0;
        background-color: #00379f;
        border: none;
        margin-top: 0;
    }

    .dropdown-item {
        color: white;
        border-radius: 0.3125rem;
        padding: 0.5rem 1rem;
    }

    .navbar .dropdown:hover .dropdown-menu {
        display: block;
    }

    .navbar .dropdown:hover .dropdown-toggle::after {
        transform: rotate(-180deg);
        transition: transform 0.3s ease;
    }

    .dropdown-item:hover,
    .dropdown-item:focus {
        background-color: #4f72b5e0;
        color: white;
    }

    .content-row .row {
        display: flex;
        align-items: stretch;
        align-items: center;
        justify-content: center;
    }

    .content-row .col-md-7,
    .content-row .col-md-5 {
        display: flex;
        flex-direction: column;
        padding-right: 2rem;
        align-items: center;
        justify-content: center;
    }
}

/*############# Navbar mobile################## */
@media (max-width: 768px) {
    .dropdown-menu {
        border-radius: 0;
        background-color: #00379f;
        border: none;
        margin-top: 0;
    }

    .dropdown-item {
        color: white;
        border-radius: 0.3125rem;
        padding: 0.5rem 1rem;
    }

    .navbar .dropdown:hover .dropdown-menu {
        display: block;
    }

    .navbar .dropdown:hover .dropdown-toggle::after {
        transform: rotate(-180deg);
        transition: transform 0.3s ease;
    }

    .dropdown-item:hover,
    .dropdown-item:focus {
        background-color: #4f72b5e0;
        color: white;
    }


    .navbar-toggler {
        border: 0;
    }

    .navbar-toggler:focus {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .navbar-brand{
        display: block;
        font-size: 1rem;
        font-style: bold;
        display: block;
        margin-top: 0.1rem;
    }
    .text-muted {
        display: block;
        font-size: 0.8rem;
        font-style: italic;
        line-height: initial;
        display: block;
        margin-top: 0.1rem;
        color: #8ca5d4;
    }
}

/* ####################### SEZIONE HOME ############################# */
.home {
    display: flex;
    padding-block-start: 8rem;
    padding-block-end: 12rem;
    padding-left: 7rem;
    padding-right: 8.5rem;
}

.image-section-home {
    margin-right: 3rem;
}

.text-section-home {
    padding-left: 4rem;
    text-align: justify;
}

.text-section-home h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: justify;
}

.text-section-home p {
    font-size: 1.2rem;
    line-height: 1.4;
    text-align: justify;
}

/* Stili comuni per .scroll-down */
.scroll-down {
    display: block;
    margin-top: 0.2rem;
    margin-bottom: 2rem;
    margin-left: auto;
    margin-right: auto;
    width: 50px;
    height: 50px;
    text-align: center;
    font-size: 2rem;
    text-decoration: none;
    color: #00379f;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-10px);
    }
    60% {
        transform: translateY(-5px);
    }
}

/* Home mobile */
@media (max-width: 768px) {
    .home {
        margin-block-start: 6.5rem !important;
        padding: 1rem !important;
    }

    .image-section-home {
        width: 100%;
        text-align: center;
        margin-bottom: 1rem;
    }

    .image-section-home img {
        width: 100%;
        height: auto;
        margin-bottom: 1.5rem;
    }

    .text-section-home {
        width: 100%;
        padding-left: 0;
        margin-bottom: 1rem;
    }

    .text-section-home h1 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        text-align: center;

    }

    .text-section-home p {
        font-size: 1.1rem;
        line-height: 1.4;
        margin-left: 2rem;
        margin-right: 2rem;
    }

    .scroll-down {
        margin-top: 1rem;
        margin-bottom: 2rem;
    }
}

/* ####################### PAGINA GRAFICI ############################# */
.graph-table-page {
    padding: 2rem;
}

/* ############ Dropdown selezione grafici ############ */
.selection-row {
    margin-bottom: 1rem;
    margin-top: 2rem;
    display: flex;
    justify-content: center;
}

.selection-row .form-select {
    margin-left: 0rem;
    width: 48%;
    padding: 0.3rem;
    background-color: #ffffff;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    font-size: 1rem;
    color: #495057;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    box-shadow: 0 0 2px rgba(0, 0, 0, 0.1);
}

.form-select {
    font-weight: 620;
    text-align: center;
}

.selection-row .form-select:focus {
    border-color: #e9ecef;
    outline: none;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
}

.text p{
    margin-right: 3.2rem;
    margin-left: 3.2rem;
    text-align: justify;
    }

.text1 p{
    margin-right: 3.2rem;
    text-align: justify;
    }
.text1 h2{
    margin-right: 3.2rem;
    margin-top: 1.5rem;
    text-align: center;
    }
.text1 h1{
    margin-right: 3.2rem;
    margin-top: 1.5rem;
    text-align: center;
    }
.text1 h3{
    margin-right: 3.2rem;
    margin-top: 1.5rem;
    text-align: center;
    }


.text3 p{
    margin-left: 3.2rem;
    text-align: justify;
    }
.text3 h2{
    margin-left: 3.2rem;
    margin-top: 1.5rem;
    text-align: center;
    }
.text3 h1{
    margin-left: 3.2rem;
    margin-top: 1.5rem;
    text-align: center;
    }
.text3 h3{
    margin-left: 3.2rem;
    margin-top: 1.5rem;
    text-align: center;
    }

/* Stili per schermi piccoli (mobile) */
@media only screen and (max-width: 768px) {
    .annotation-text {
        font-size: 8px; /* Ridimensiona il testo per il mobile */
    }

    .bg {
        height: 16px; /* Riduci l'altezza del rettangolo di sfondo */
        width: 100%; /* Adatta la larghezza del rettangolo di sfondo */
    }
}

/* ############ Dropdown per mobile ############*/
@media (max-width: 768px) {
    .selection-row .form-select {
        font-size: 0.875rem;
        padding: 0.5rem;
        width: 100%;
        margin-left: 1rem;
        margin-right: 1rem;
    }
    h2 {
        margin-right: 1rem;
        margin-left: 1rem;
        text-align: center;
    }
    h1 {
        margin-right: 1rem;
        margin-left: 1rem;
        text-align: justify;
    }
    .text p{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: justify;
    }
    .text1 p{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: justify;
    }
    .text1 h2{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: center;
    }
    .text1 h1{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: center;
    }


    .text2 p{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: justify;
    }
    .text2 h2{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: center;
    }
    .text2 h1{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: center;
    }

    .text3 p{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: justify;
    }
    .text3 h2{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: center;
    }
    .text3 h1{
       margin-right: 1rem;
       margin-left: 1rem;
       text-align: center;
    }
}


/* ####################### TABLE ############################# */

.table-container {
       overflow-y: auto; /* Abilita lo scorrimento verticale su dispositivi mobili */
       max-height: 20rem; /* Limita l'altezza massima della tabella per scorrimento verticale */
       width: 100%;
       overflow-x: auto;
       margin-bottom: 1rem;
       margin-top: 3rem;

    }

.table-container table {
    width: 100%;
    margin-bottom: 1rem;
    background-color: transparent;
    border-collapse: collapse;
    border: 0;
}

.table-container th,
.table-container td {
    padding: 0.75rem;
    vertical-align: top;
    border-top: 1px solid #dee2e6;
    text-align: center;
}

.table-container th {
    border-top: 0;
    border-bottom: 2px solid #dee2e6;
}

.table-container tbody tr:hover {
    background-color: #f5f5f5;
}

/* ############ Scrollbar personalizzata ############ */
.table-container::-webkit-scrollbar {
    width: 8px;
}

.table-container::-webkit-scrollbar-thumb {
    background-color: #808080;
    border-radius: 10px;
    border: 2px solid transparent;
    height: 20%;
    min-height: 1rem;
}



.table-container::-webkit-scrollbar-track {
    background-color: transparent;
}

.table-container::-webkit-scrollbar-thumb:active {
    background-color: #808080;
}
.col-sm-12.col-md-5.table-scrollable {
    max-height: 10rem; /* Limita l'altezza massima per lo scroll verticale */
    overflow-y: auto; /* Abilita lo scorrimento verticale */
    display: flex;

    }

/* ############Table mobile ############ */
@media (max-width: 768px) {
    .row.graph-page {
        padding-bottom: 2rem;
    }



    .table-container th,
    .table-container td {
        white-space: nowrap;
    }
}


    </style>

</head>
<body>

<!-- nav-bar menu -->
<nav class="navbar navbar-expand-lg navbar-dark fixed-top" style="background-color: #00379f;">
    <div class="container-fluid">
        <a class="navbar-brand" href="#paginaHome">INTERFACCIA
            <small class="text-muted">Interactive Dashboard</small>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown"
                aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="navbarNavDropdown">
            <ul class="navbar-nav">
                
                    
                    <li class="nav-item">
                        <a class="nav-link" href="#home">Home</a>
                    </li>
                    
                
                    
                    <li class="nav-item">
                        <a class="nav-link" href="#abc">Page One</a>
                    </li>
                    
                
                    
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="abcdDropdown" role="button"
                           data-bs-toggle="dropdown" aria-expanded="false">
                            Dropdow
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="abcdDropdown">
                            
                                <li><a class="dropdown-item" href="#abcde">Page two</a></li>
                            
                                <li><a class="dropdown-item" href="#abcdef">Page  three</a></li>
                            
                        </ul>
                    </li>
                    
                
                    
                    <li class="nav-item">
                        <a class="nav-link" href="#note">Repositories</a>
                    </li>
                    
                
            </ul>
        </div>
    </div>
</nav>

<!-- pages -->


    <!-- Home -->
    
        <div id="home" class="home" style="display:flex;">
            <div class="row align-items-center">
                <div class="col-sm-12 col-md-6">
                    <div class="image-section-home">
                        <img src="https://raw.githubusercontent.com/fr-cm/interfaccia/main/Tutorial/img/interfaccia_1.png" alt="Logo" style="max-width: 90%; height: auto">
                    </div>
                </div>
                <div class="col-sm-12 col-md-6">
                    <div class="text-section-home">
                        <h1>Welcome to the Interfaccia Dashboard</h1>
                        <p><p>This <a href="https://github.com/fr-cm/interfaccia">repository</a> is designed to streamline the process of creating a modular, multi-device dashboard with simulated interactivity while minimizing Python code. It features functions that automate the creation of charts and tables, and it provides automatic download links for CSV files, allowing users to download data without the need for server storage. Additionally, it addresses the issue of resizing Plotly charts when display is set to none. Check out the pages below to explore its various features and capabilities.</p></p>
                    </div>
                </div>
                <div class="scroll-down">
                    <a href="#next-section" class="scroll-down">
                        &#x25BC;
                    </a>
                </div>
                <div id="next-section" class="next-section"></div>
            </div>
        </div>

    <!-- page_menu -->
    



    <!-- Home -->
    
        <div id="abc" class="page-menu">
            <h2>Page Menù</h2>
            <div id="content-page-abc">
                <div class="selection-row">
                    <select class="form-select" id="page-selector-abc"
                            onchange="updateDisplay('abc', this.value)">
                        
                            <option value="1">chart,table and download</option>
                        
                            <option value="2">chart and table</option>
                        
                            <option value="3">chart, text and download</option>
                        
                            <option value="4">chart and text</option>
                        
                            <option value="5">text</option>
                        
                            <option value="6">image</option>
                        
                            <option value="7">image and text</option>
                        
                            <option value="8">text and image</option>
                        
                            <option value="9">table</option>
                        
                            <option value="10">chart</option>
                        
                            <option value="11">chart and download</option>
                        
                    </select>
                </div>
                <div class="content-row" id="content-row-abc">
                    
                    <div class="row" id="1" style="display: block;">
                        
                        <div class=" col-sm-12 col-md-7">
                            <div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.34.0.min.js"></script>                <div id="3d225dcd-1129-4309-b15a-120880634472" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("3d225dcd-1129-4309-b15a-120880634472")) {                    Plotly.newPlot(                        "3d225dcd-1129-4309-b15a-120880634472",                        [{"marker":{"color":"#00379f"},"name":"Bar Data","orientation":"v","width":1,"x":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99],"xaxis":"x","y":[1.764052345967664,0.4001572083672233,0.9787379841057392,2.240893199201458,1.8675579901499675,-0.977277879876411,0.9500884175255894,-0.1513572082976979,-0.10321885179355784,0.41059850193837233,0.144043571160878,1.454273506962975,0.7610377251469934,0.12167501649282841,0.44386323274542566,0.33367432737426683,1.4940790731576061,-0.20515826376580087,0.31306770165090136,-0.8540957393017248,-2.5529898158340787,0.6536185954403606,0.8644361988595057,-0.7421650204064419,2.2697546239876076,-1.4543656745987648,0.04575851730144607,-0.1871838500258336,1.5327792143584575,1.469358769900285,0.1549474256969163,0.37816251960217356,-0.8877857476301128,-1.980796468223927,-0.3479121493261526,0.15634896910398005,1.2302906807277207,1.2023798487844113,-0.3873268174079523,-0.30230275057533557,-1.0485529650670926,-1.4200179371789752,-1.7062701906250126,1.9507753952317897,-0.5096521817516535,-0.4380743016111864,-1.2527953600499262,0.7774903558319101,-1.6138978475579515,-0.2127402802139687,-0.8954665611936756,0.386902497859262,-0.510805137568873,-1.180632184122412,-0.028182228338654868,0.42833187053041766,0.06651722238316789,0.3024718977397814,-0.6343220936809636,-0.3627411659871381,-0.672460447775951,-0.3595531615405413,-0.813146282044454,-1.7262826023316769,0.17742614225375283,-0.4017809362082619,-1.6301983469660446,0.4627822555257742,-0.9072983643832422,0.05194539579613895,0.7290905621775369,0.12898291075741067,1.1394006845433007,-1.2348258203536526,0.402341641177549,-0.6848100909403132,-0.8707971491818818,-0.5788496647644155,-0.31155253212737266,0.05616534222974544,-1.1651498407833565,0.9008264869541871,0.46566243973045984,-1.5362436862772237,1.4882521937955997,1.8958891760305832,1.1787795711596507,-0.17992483581235091,-1.0707526215105425,1.0544517269311366,-0.40317694697317963,1.2224450703824274,0.2082749780768603,0.9766390364837128,0.3563663971744019,0.7065731681919482,0.010500020720820478,1.7858704939058352,0.12691209270361992,0.40198936344470165],"yaxis":"y","type":"bar"},{"line":{"color":"#007eff","width":1},"mode":"lines","name":"Line Data","x":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99],"xaxis":"x2","y":[4,8,6,4,8,6,4,4,5,2,4,5,4,5,4,5,7,3,5,3,6,5,5,4,3,5,4,7,6,6,7,3,5,5,8,4,4,3,2,7,6,6,4,5,3,5,8,7,4,8,4,8,7,6,6,7,4,7,5,2,4,3,8,5,5,6,4,3,6,4,5,4,3,7,8,8,7,6,4,3,5,4,3,2,6,2,6,3,3,3,6,4,5,5,7,6,4,3,3,4],"yaxis":"y","type":"scatter"}],                        {"template":{"layout":{"colorway":["#00379f","#007eff","#7bd200","#35009f","#0174af","#db5700","#bbd64a","#a9a3d0","#007eff","#7bd200","#db5700","#ffc000","#403152","#bfbfbf","#00b050","#cc66cd","#00379f","#00b0f0","#92cddc"],"font":{"family":"Arial"}}},"title":{"text":"","x":0.5},"xaxis":{"title":{"text":"X Axis"},"tickmode":"array"},"legend":{"x":0.5,"y":1.15,"xanchor":"center","yanchor":"top","orientation":"h"},"yaxis":{"title":{"text":"Y Axis"}},"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)","plot_bgcolor":"rgba(0,0,0,0)","showlegend":true,"annotations":[{"align":"center","font":{"color":"gray","size":10},"showarrow":false,"text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yanchor":"top","yref":"paper"}],"xaxis2":{"overlaying":"x","side":"top"}},                        {"responsive": true}                    )                };                            </script>        </div>
                        </div>
                        <div class="col-sm-12 col-md-5">
                            <div class="table-container table-sm table-scrollable" border="0" index="false">
                                <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>a</th>      <th>b</th>      <th>c</th>    </tr>  </thead>  <tbody>    <tr>      <td>0</td>      <td>1.764052</td>      <td>4</td>    </tr>    <tr>      <td>1</td>      <td>0.400157</td>      <td>8</td>    </tr>    <tr>      <td>2</td>      <td>0.978738</td>      <td>6</td>    </tr>    <tr>      <td>3</td>      <td>2.240893</td>      <td>4</td>    </tr>    <tr>      <td>4</td>      <td>1.867558</td>      <td>8</td>    </tr>    <tr>      <td>5</td>      <td>-0.977278</td>      <td>6</td>    </tr>    <tr>      <td>6</td>      <td>0.950088</td>      <td>4</td>    </tr>    <tr>      <td>7</td>      <td>-0.151357</td>      <td>4</td>    </tr>    <tr>      <td>8</td>      <td>-0.103219</td>      <td>5</td>    </tr>    <tr>      <td>9</td>      <td>0.410599</td>      <td>2</td>    </tr>    <tr>      <td>10</td>      <td>0.144044</td>      <td>4</td>    </tr>    <tr>      <td>11</td>      <td>1.454274</td>      <td>5</td>    </tr>    <tr>      <td>12</td>      <td>0.761038</td>      <td>4</td>    </tr>    <tr>      <td>13</td>      <td>0.121675</td>      <td>5</td>    </tr>    <tr>      <td>14</td>      <td>0.443863</td>      <td>4</td>    </tr>    <tr>      <td>15</td>      <td>0.333674</td>      <td>5</td>    </tr>    <tr>      <td>16</td>      <td>1.494079</td>      <td>7</td>    </tr>    <tr>      <td>17</td>      <td>-0.205158</td>      <td>3</td>    </tr>    <tr>      <td>18</td>      <td>0.313068</td>      <td>5</td>    </tr>    <tr>      <td>19</td>      <td>-0.854096</td>      <td>3</td>    </tr>    <tr>      <td>20</td>      <td>-2.552990</td>      <td>6</td>    </tr>    <tr>      <td>21</td>      <td>0.653619</td>      <td>5</td>    </tr>    <tr>      <td>22</td>      <td>0.864436</td>      <td>5</td>    </tr>    <tr>      <td>23</td>      <td>-0.742165</td>      <td>4</td>    </tr>    <tr>      <td>24</td>      <td>2.269755</td>      <td>3</td>    </tr>    <tr>      <td>25</td>      <td>-1.454366</td>      <td>5</td>    </tr>    <tr>      <td>26</td>      <td>0.045759</td>      <td>4</td>    </tr>    <tr>      <td>27</td>      <td>-0.187184</td>      <td>7</td>    </tr>    <tr>      <td>28</td>      <td>1.532779</td>      <td>6</td>    </tr>    <tr>      <td>29</td>      <td>1.469359</td>      <td>6</td>    </tr>    <tr>      <td>30</td>      <td>0.154947</td>      <td>7</td>    </tr>    <tr>      <td>31</td>      <td>0.378163</td>      <td>3</td>    </tr>    <tr>      <td>32</td>      <td>-0.887786</td>      <td>5</td>    </tr>    <tr>      <td>33</td>      <td>-1.980796</td>      <td>5</td>    </tr>    <tr>      <td>34</td>      <td>-0.347912</td>      <td>8</td>    </tr>    <tr>      <td>35</td>      <td>0.156349</td>      <td>4</td>    </tr>    <tr>      <td>36</td>      <td>1.230291</td>      <td>4</td>    </tr>    <tr>      <td>37</td>      <td>1.202380</td>      <td>3</td>    </tr>    <tr>      <td>38</td>      <td>-0.387327</td>      <td>2</td>    </tr>    <tr>      <td>39</td>      <td>-0.302303</td>      <td>7</td>    </tr>    <tr>      <td>40</td>      <td>-1.048553</td>      <td>6</td>    </tr>    <tr>      <td>41</td>      <td>-1.420018</td>      <td>6</td>    </tr>    <tr>      <td>42</td>      <td>-1.706270</td>      <td>4</td>    </tr>    <tr>      <td>43</td>      <td>1.950775</td>      <td>5</td>    </tr>    <tr>      <td>44</td>      <td>-0.509652</td>      <td>3</td>    </tr>    <tr>      <td>45</td>      <td>-0.438074</td>      <td>5</td>    </tr>    <tr>      <td>46</td>      <td>-1.252795</td>      <td>8</td>    </tr>    <tr>      <td>47</td>      <td>0.777490</td>      <td>7</td>    </tr>    <tr>      <td>48</td>      <td>-1.613898</td>      <td>4</td>    </tr>    <tr>      <td>49</td>      <td>-0.212740</td>      <td>8</td>    </tr>    <tr>      <td>50</td>      <td>-0.895467</td>      <td>4</td>    </tr>    <tr>      <td>51</td>      <td>0.386902</td>      <td>8</td>    </tr>    <tr>      <td>52</td>      <td>-0.510805</td>      <td>7</td>    </tr>    <tr>      <td>53</td>      <td>-1.180632</td>      <td>6</td>    </tr>    <tr>      <td>54</td>      <td>-0.028182</td>      <td>6</td>    </tr>    <tr>      <td>55</td>      <td>0.428332</td>      <td>7</td>    </tr>    <tr>      <td>56</td>      <td>0.066517</td>      <td>4</td>    </tr>    <tr>      <td>57</td>      <td>0.302472</td>      <td>7</td>    </tr>    <tr>      <td>58</td>      <td>-0.634322</td>      <td>5</td>    </tr>    <tr>      <td>59</td>      <td>-0.362741</td>      <td>2</td>    </tr>    <tr>      <td>60</td>      <td>-0.672460</td>      <td>4</td>    </tr>    <tr>      <td>61</td>      <td>-0.359553</td>      <td>3</td>    </tr>    <tr>      <td>62</td>      <td>-0.813146</td>      <td>8</td>    </tr>    <tr>      <td>63</td>      <td>-1.726283</td>      <td>5</td>    </tr>    <tr>      <td>64</td>      <td>0.177426</td>      <td>5</td>    </tr>    <tr>      <td>65</td>      <td>-0.401781</td>      <td>6</td>    </tr>    <tr>      <td>66</td>      <td>-1.630198</td>      <td>4</td>    </tr>    <tr>      <td>67</td>      <td>0.462782</td>      <td>3</td>    </tr>    <tr>      <td>68</td>      <td>-0.907298</td>      <td>6</td>    </tr>    <tr>      <td>69</td>      <td>0.051945</td>      <td>4</td>    </tr>    <tr>      <td>70</td>      <td>0.729091</td>      <td>5</td>    </tr>    <tr>      <td>71</td>      <td>0.128983</td>      <td>4</td>    </tr>    <tr>      <td>72</td>      <td>1.139401</td>      <td>3</td>    </tr>    <tr>      <td>73</td>      <td>-1.234826</td>      <td>7</td>    </tr>    <tr>      <td>74</td>      <td>0.402342</td>      <td>8</td>    </tr>    <tr>      <td>75</td>      <td>-0.684810</td>      <td>8</td>    </tr>    <tr>      <td>76</td>      <td>-0.870797</td>      <td>7</td>    </tr>    <tr>      <td>77</td>      <td>-0.578850</td>      <td>6</td>    </tr>    <tr>      <td>78</td>      <td>-0.311553</td>      <td>4</td>    </tr>    <tr>      <td>79</td>      <td>0.056165</td>      <td>3</td>    </tr>    <tr>      <td>80</td>      <td>-1.165150</td>      <td>5</td>    </tr>    <tr>      <td>81</td>      <td>0.900826</td>      <td>4</td>    </tr>    <tr>      <td>82</td>      <td>0.465662</td>      <td>3</td>    </tr>    <tr>      <td>83</td>      <td>-1.536244</td>      <td>2</td>    </tr>    <tr>      <td>84</td>      <td>1.488252</td>      <td>6</td>    </tr>    <tr>      <td>85</td>      <td>1.895889</td>      <td>2</td>    </tr>    <tr>      <td>86</td>      <td>1.178780</td>      <td>6</td>    </tr>    <tr>      <td>87</td>      <td>-0.179925</td>      <td>3</td>    </tr>    <tr>      <td>88</td>      <td>-1.070753</td>      <td>3</td>    </tr>    <tr>      <td>89</td>      <td>1.054452</td>      <td>3</td>    </tr>    <tr>      <td>90</td>      <td>-0.403177</td>      <td>6</td>    </tr>    <tr>      <td>91</td>      <td>1.222445</td>      <td>4</td>    </tr>    <tr>      <td>92</td>      <td>0.208275</td>      <td>5</td>    </tr>    <tr>      <td>93</td>      <td>0.976639</td>      <td>5</td>    </tr>    <tr>      <td>94</td>      <td>0.356366</td>      <td>7</td>    </tr>    <tr>      <td>95</td>      <td>0.706573</td>      <td>6</td>    </tr>    <tr>      <td>96</td>      <td>0.010500</td>      <td>4</td>    </tr>    <tr>      <td>97</td>      <td>1.785870</td>      <td>3</td>    </tr>    <tr>      <td>98</td>      <td>0.126912</td>      <td>3</td>    </tr>    <tr>      <td>99</td>      <td>0.401989</td>      <td>4</td>    </tr>  </tbody></table>
                            </div>
                        </div>
                        <div class="download">
                            <button onclick="downloadCSV('1')">Download</button>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="2" style="display: none;">
                        
                        <div class=" col-sm-12 col-md-7">
                            <div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.34.0.min.js"></script>                <div id="2856f0e0-a8cc-4007-b59c-8129c2e03ced" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("2856f0e0-a8cc-4007-b59c-8129c2e03ced")) {                    Plotly.newPlot(                        "2856f0e0-a8cc-4007-b59c-8129c2e03ced",                        [{"marker":{"color":"#00379f"},"name":"Bar Chart Value1","orientation":"v","width":1,"x":["Group2","Group3","Group1","Group2","Group2","Group2","Group1","Group3","Group3","Group2","Group1","Group3","Group2","Group3","Group3","Group1","Group2","Group3","Group3","Group1"],"xaxis":"x","y":[15,53,72,30,6,15,80,52,33,24,92,7,74,66,76,88,71,41,61,37],"yaxis":"y","type":"bar"},{"marker":{"color":"#007eff"},"name":"Bar Chart Value2","orientation":"v","width":1,"x":["Group2","Group3","Group1","Group2","Group2","Group2","Group1","Group3","Group3","Group2","Group1","Group3","Group2","Group3","Group3","Group1","Group2","Group3","Group3","Group1"],"xaxis":"x","y":[13,36,63,70,63,59,77,19,1,2,85,78,91,22,79,14,68,18,6,27],"yaxis":"y","type":"bar"}],                        {"template":{"layout":{"colorway":["#00379f","#007eff","#7bd200","#35009f","#0174af","#db5700","#bbd64a","#a9a3d0","#007eff","#7bd200","#db5700","#ffc000","#403152","#bfbfbf","#00b050","#cc66cd","#00379f","#00b0f0","#92cddc"],"font":{"family":"Arial"}}},"title":{"text":"","x":0.5},"xaxis":{"title":{"text":"Group"},"tickmode":"array"},"legend":{"x":0.5,"y":1.15,"xanchor":"center","yanchor":"top","orientation":"h"},"yaxis":{"title":{"text":"Value1"}},"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)","plot_bgcolor":"rgba(0,0,0,0)","showlegend":true,"annotations":[{"align":"center","font":{"color":"gray","size":10},"showarrow":false,"text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yanchor":"top","yref":"paper"}]},                        {"responsive": true}                    )                };                            </script>        </div>
                        </div>
                        <div class="col-sm-12 col-md-5">
                            <div class="table-container table-sm table-scrollable" border="0" index="false">
                                <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Group</th>      <th>Value1</th>      <th>Value2</th>    </tr>  </thead>  <tbody>    <tr>      <td>Group2</td>      <td>15</td>      <td>13</td>    </tr>    <tr>      <td>Group3</td>      <td>53</td>      <td>36</td>    </tr>    <tr>      <td>Group1</td>      <td>72</td>      <td>63</td>    </tr>    <tr>      <td>Group2</td>      <td>30</td>      <td>70</td>    </tr>    <tr>      <td>Group2</td>      <td>6</td>      <td>63</td>    </tr>    <tr>      <td>Group2</td>      <td>15</td>      <td>59</td>    </tr>    <tr>      <td>Group1</td>      <td>80</td>      <td>77</td>    </tr>    <tr>      <td>Group3</td>      <td>52</td>      <td>19</td>    </tr>    <tr>      <td>Group3</td>      <td>33</td>      <td>1</td>    </tr>    <tr>      <td>Group2</td>      <td>24</td>      <td>2</td>    </tr>    <tr>      <td>Group1</td>      <td>92</td>      <td>85</td>    </tr>    <tr>      <td>Group3</td>      <td>7</td>      <td>78</td>    </tr>    <tr>      <td>Group2</td>      <td>74</td>      <td>91</td>    </tr>    <tr>      <td>Group3</td>      <td>66</td>      <td>22</td>    </tr>    <tr>      <td>Group3</td>      <td>76</td>      <td>79</td>    </tr>    <tr>      <td>Group1</td>      <td>88</td>      <td>14</td>    </tr>    <tr>      <td>Group2</td>      <td>71</td>      <td>68</td>    </tr>    <tr>      <td>Group3</td>      <td>41</td>      <td>18</td>    </tr>    <tr>      <td>Group3</td>      <td>61</td>      <td>6</td>    </tr>    <tr>      <td>Group1</td>      <td>37</td>      <td>27</td>    </tr>  </tbody></table>
                            </div>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="3" style="display: none;">
                        
                        <div class="col-md-7 col-sm-12 ">
                            <div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.34.0.min.js"></script>                <div id="72964632-b93f-49a0-95fe-7f8cadb97770" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("72964632-b93f-49a0-95fe-7f8cadb97770")) {                    Plotly.newPlot(                        "72964632-b93f-49a0-95fe-7f8cadb97770",                        [{"line":{"color":"#00379f","width":1},"mode":"lines","name":"Sales Over Time","x":["2023-01-01T00:00:00","2023-01-02T00:00:00","2023-01-03T00:00:00","2023-01-04T00:00:00","2023-01-05T00:00:00","2023-01-06T00:00:00","2023-01-07T00:00:00","2023-01-08T00:00:00","2023-01-09T00:00:00","2023-01-10T00:00:00","2023-01-11T00:00:00","2023-01-12T00:00:00","2023-01-13T00:00:00","2023-01-14T00:00:00","2023-01-15T00:00:00","2023-01-16T00:00:00","2023-01-17T00:00:00","2023-01-18T00:00:00","2023-01-19T00:00:00","2023-01-20T00:00:00","2023-01-21T00:00:00","2023-01-22T00:00:00","2023-01-23T00:00:00","2023-01-24T00:00:00","2023-01-25T00:00:00","2023-01-26T00:00:00","2023-01-27T00:00:00","2023-01-28T00:00:00","2023-01-29T00:00:00","2023-01-30T00:00:00","2023-01-31T00:00:00","2023-02-01T00:00:00","2023-02-02T00:00:00","2023-02-03T00:00:00","2023-02-04T00:00:00","2023-02-05T00:00:00","2023-02-06T00:00:00","2023-02-07T00:00:00","2023-02-08T00:00:00","2023-02-09T00:00:00","2023-02-10T00:00:00","2023-02-11T00:00:00","2023-02-12T00:00:00","2023-02-13T00:00:00","2023-02-14T00:00:00","2023-02-15T00:00:00","2023-02-16T00:00:00","2023-02-17T00:00:00","2023-02-18T00:00:00","2023-02-19T00:00:00","2023-02-20T00:00:00","2023-02-21T00:00:00","2023-02-22T00:00:00","2023-02-23T00:00:00","2023-02-24T00:00:00","2023-02-25T00:00:00","2023-02-26T00:00:00","2023-02-27T00:00:00","2023-02-28T00:00:00","2023-03-01T00:00:00","2023-03-02T00:00:00","2023-03-03T00:00:00","2023-03-04T00:00:00","2023-03-05T00:00:00","2023-03-06T00:00:00","2023-03-07T00:00:00","2023-03-08T00:00:00","2023-03-09T00:00:00","2023-03-10T00:00:00","2023-03-11T00:00:00","2023-03-12T00:00:00","2023-03-13T00:00:00","2023-03-14T00:00:00","2023-03-15T00:00:00","2023-03-16T00:00:00","2023-03-17T00:00:00","2023-03-18T00:00:00","2023-03-19T00:00:00","2023-03-20T00:00:00","2023-03-21T00:00:00","2023-03-22T00:00:00","2023-03-23T00:00:00","2023-03-24T00:00:00","2023-03-25T00:00:00","2023-03-26T00:00:00","2023-03-27T00:00:00","2023-03-28T00:00:00","2023-03-29T00:00:00","2023-03-30T00:00:00","2023-03-31T00:00:00","2023-04-01T00:00:00","2023-04-02T00:00:00","2023-04-03T00:00:00","2023-04-04T00:00:00","2023-04-05T00:00:00","2023-04-06T00:00:00","2023-04-07T00:00:00","2023-04-08T00:00:00","2023-04-09T00:00:00","2023-04-10T00:00:00"],"xaxis":"x","y":[273,267,133,453,421,301,187,424,380,106,453,470,355,160,316,161,287,221,385,339,128,252,487,249,362,184,377,219,383,466,487,409,393,107,476,436,239,486,410,105,373,350,481,178,489,434,181,333,210,208,130,454,359,228,449,400,272,336,483,215,354,100,373,191,328,287,121,163,322,201,245,138,307,485,243,314,337,117,336,214,275,294,367,493,396,147,360,494,354,234,474,428,492,300,329,118,102,297,321,329],"yaxis":"y","type":"scatter"},{"line":{"color":"#007eff","width":1},"mode":"lines","name":"Expenses Over Time","x":["2023-01-01T00:00:00","2023-01-02T00:00:00","2023-01-03T00:00:00","2023-01-04T00:00:00","2023-01-05T00:00:00","2023-01-06T00:00:00","2023-01-07T00:00:00","2023-01-08T00:00:00","2023-01-09T00:00:00","2023-01-10T00:00:00","2023-01-11T00:00:00","2023-01-12T00:00:00","2023-01-13T00:00:00","2023-01-14T00:00:00","2023-01-15T00:00:00","2023-01-16T00:00:00","2023-01-17T00:00:00","2023-01-18T00:00:00","2023-01-19T00:00:00","2023-01-20T00:00:00","2023-01-21T00:00:00","2023-01-22T00:00:00","2023-01-23T00:00:00","2023-01-24T00:00:00","2023-01-25T00:00:00","2023-01-26T00:00:00","2023-01-27T00:00:00","2023-01-28T00:00:00","2023-01-29T00:00:00","2023-01-30T00:00:00","2023-01-31T00:00:00","2023-02-01T00:00:00","2023-02-02T00:00:00","2023-02-03T00:00:00","2023-02-04T00:00:00","2023-02-05T00:00:00","2023-02-06T00:00:00","2023-02-07T00:00:00","2023-02-08T00:00:00","2023-02-09T00:00:00","2023-02-10T00:00:00","2023-02-11T00:00:00","2023-02-12T00:00:00","2023-02-13T00:00:00","2023-02-14T00:00:00","2023-02-15T00:00:00","2023-02-16T00:00:00","2023-02-17T00:00:00","2023-02-18T00:00:00","2023-02-19T00:00:00","2023-02-20T00:00:00","2023-02-21T00:00:00","2023-02-22T00:00:00","2023-02-23T00:00:00","2023-02-24T00:00:00","2023-02-25T00:00:00","2023-02-26T00:00:00","2023-02-27T00:00:00","2023-02-28T00:00:00","2023-03-01T00:00:00","2023-03-02T00:00:00","2023-03-03T00:00:00","2023-03-04T00:00:00","2023-03-05T00:00:00","2023-03-06T00:00:00","2023-03-07T00:00:00","2023-03-08T00:00:00","2023-03-09T00:00:00","2023-03-10T00:00:00","2023-03-11T00:00:00","2023-03-12T00:00:00","2023-03-13T00:00:00","2023-03-14T00:00:00","2023-03-15T00:00:00","2023-03-16T00:00:00","2023-03-17T00:00:00","2023-03-18T00:00:00","2023-03-19T00:00:00","2023-03-20T00:00:00","2023-03-21T00:00:00","2023-03-22T00:00:00","2023-03-23T00:00:00","2023-03-24T00:00:00","2023-03-25T00:00:00","2023-03-26T00:00:00","2023-03-27T00:00:00","2023-03-28T00:00:00","2023-03-29T00:00:00","2023-03-30T00:00:00","2023-03-31T00:00:00","2023-04-01T00:00:00","2023-04-02T00:00:00","2023-04-03T00:00:00","2023-04-04T00:00:00","2023-04-05T00:00:00","2023-04-06T00:00:00","2023-04-07T00:00:00","2023-04-08T00:00:00","2023-04-09T00:00:00","2023-04-10T00:00:00"],"xaxis":"x","y":[150,156,207,205,195,236,189,99,122,138,53,162,61,107,228,193,235,181,168,278,238,217,263,207,231,117,106,253,169,129,95,140,129,275,61,297,183,208,236,118,109,82,87,221,175,110,95,79,205,281,77,79,176,122,125,147,256,88,61,252,296,139,82,228,90,248,80,200,173,125,85,262,246,113,54,227,166,207,241,111,141,161,261,154,140,76,123,228,273,144,67,249,106,293,85,251,270,97,98,169],"yaxis":"y","type":"scatter"}],                        {"template":{"layout":{"colorway":["#00379f","#007eff","#7bd200","#35009f","#0174af","#db5700","#bbd64a","#a9a3d0","#007eff","#7bd200","#db5700","#ffc000","#403152","#bfbfbf","#00b050","#cc66cd","#00379f","#00b0f0","#92cddc"],"font":{"family":"Arial"}}},"title":{"text":"","x":0.5},"xaxis":{"title":{"text":"Date"},"tickmode":"array"},"legend":{"x":0.5,"y":1.15,"xanchor":"center","yanchor":"top","orientation":"h"},"yaxis":{"title":{"text":"Sales"}},"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)","plot_bgcolor":"rgba(0,0,0,0)","showlegend":true,"annotations":[{"align":"center","font":{"color":"gray","size":10},"showarrow":false,"text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yanchor":"top","yref":"paper"}]},                        {"responsive": true}                    )                };                            </script>        </div>
                        </div>

                        <div class=" col-md-5 col-sm-12 text1">
                            <h3><h3> Lorem ipsum dolor sit amet, consectetur adipiscing elit.</h3></h3>
                            <p><p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. </p></p>
                        </div>
                        <div class="download">
                            <button onclick="downloadCSV('3')">Download</button>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="4" style="display: none;">
                        
                        <div class=" col-md-7 col-sm-12 ">
                            <div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.34.0.min.js"></script>                <div id="ffa062a8-79b8-4fd8-b52a-0a73024ed961" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("ffa062a8-79b8-4fd8-b52a-0a73024ed961")) {                    Plotly.newPlot(                        "ffa062a8-79b8-4fd8-b52a-0a73024ed961",                        [{"hole":0,"labels":["D","D","D","A","C","D","D","C","C","D","B","B","B","B","A","B","D","D","D","B","C","D","B","A","A","D","C","A","B","B","A","D","D","A","B","C","B","C","C","A","D","C","B","D","D","B","A","D","C","B"],"name":"pie Chart","values":[7,6,2,8,4,5,8,1,4,6,7,7,8,5,8,3,1,2,7,6,5,9,8,9,7,2,5,9,6,2,7,3,8,6,8,7,7,4,4,5,5,2,4,6,2,8,6,5,3,1],"type":"pie"}],                        {"template":{"layout":{"colorway":["#00379f","#007eff","#7bd200","#35009f","#0174af","#db5700","#bbd64a","#a9a3d0","#007eff","#7bd200","#db5700","#ffc000","#403152","#bfbfbf","#00b050","#cc66cd","#00379f","#00b0f0","#92cddc"],"font":{"family":"Arial"}}},"title":{"text":"","x":0.5},"xaxis":{"title":{"text":"Category"},"tickmode":"array"},"legend":{"x":0.5,"y":1.15,"xanchor":"center","yanchor":"top","orientation":"h"},"yaxis":{"title":{"text":"Values"}},"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)","plot_bgcolor":"rgba(0,0,0,0)","showlegend":true,"annotations":[{"align":"center","font":{"color":"gray","size":10},"showarrow":false,"text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yanchor":"top","yref":"paper"}]},                        {"responsive": true}                    )                };                            </script>        </div>
                        </div>
                        <div class=" col-md-5 col-sm-12 text1">
                            <h3><h3> Lorem ipsum dolor sit amet, consectetur adipiscing elit.</h3></h3>
                            <p><p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. </p></p>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="5" style="display: none;">
                        
                        <div class="col-sm-12 col-ms-12 text">
                            <h3><h2>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</h2></h3>
                            <p><p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. </p></p>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="6" style="display: none;">
                        
                        <div class="img1 col-sm-12 col-md-12">
                            <img src="https://raw.githubusercontent.com/fr-cm/interfaccia/main/Tutorial/img/interfaccia_1.png" alt="Image" style="max-width: 100%; height: auto;">
                        </div>
                        
                    </div>
                    
                    <div class="row" id="7" style="display: none;">
                        
                        <div class="img2 col-md-7 col-sm-12 ">
                            <img src="https://raw.githubusercontent.com/fr-cm/interfaccia/main/Tutorial/img/img_4.png" alt="Image" style="max-width: 100%; height: auto;">
                        </div>
                        <div class="col-md-5 col-sm-12 text1">
                            <h2><h3> Lorem ipsum dolor sit amet, consectetur adipiscing elit.</h3></h2>
                            <p><p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. </p></p>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="8" style="display: none;">
                        
                        <div class="col-md-7 col-sm-12 text3">
                            <h2><h3> Lorem sed iaculis leo dictum. </h3></h2>
                            <p><p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. </p></p>
                        </div>
                        <div class="img2 col-md-5 col-sm-12 ">
                            <img src="https://raw.githubusercontent.com/fr-cm/interfaccia/main/Tutorial/img/img_1.png" alt="Image" style="max-width: 100%; height: auto;">
                        </div>
                        
                    </div>
                    
                    <div class="row" id="9" style="display: none;">
                        
                        <div class="col-sm-12 col-md-12 table-large">
                            <div class="table-container table-sm table-scrollable" border="0" index="false"
                                 style="text-align: justify;    overflow-x: hidden; ">
                                <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>Date</th>      <th>Sales</th>      <th>Expenses</th>    </tr>  </thead>  <tbody>    <tr>      <td>2023-01-01</td>      <td>273</td>      <td>150</td>    </tr>    <tr>      <td>2023-01-02</td>      <td>267</td>      <td>156</td>    </tr>    <tr>      <td>2023-01-03</td>      <td>133</td>      <td>207</td>    </tr>    <tr>      <td>2023-01-04</td>      <td>453</td>      <td>205</td>    </tr>    <tr>      <td>2023-01-05</td>      <td>421</td>      <td>195</td>    </tr>    <tr>      <td>2023-01-06</td>      <td>301</td>      <td>236</td>    </tr>    <tr>      <td>2023-01-07</td>      <td>187</td>      <td>189</td>    </tr>    <tr>      <td>2023-01-08</td>      <td>424</td>      <td>99</td>    </tr>    <tr>      <td>2023-01-09</td>      <td>380</td>      <td>122</td>    </tr>    <tr>      <td>2023-01-10</td>      <td>106</td>      <td>138</td>    </tr>    <tr>      <td>2023-01-11</td>      <td>453</td>      <td>53</td>    </tr>    <tr>      <td>2023-01-12</td>      <td>470</td>      <td>162</td>    </tr>    <tr>      <td>2023-01-13</td>      <td>355</td>      <td>61</td>    </tr>    <tr>      <td>2023-01-14</td>      <td>160</td>      <td>107</td>    </tr>    <tr>      <td>2023-01-15</td>      <td>316</td>      <td>228</td>    </tr>    <tr>      <td>2023-01-16</td>      <td>161</td>      <td>193</td>    </tr>    <tr>      <td>2023-01-17</td>      <td>287</td>      <td>235</td>    </tr>    <tr>      <td>2023-01-18</td>      <td>221</td>      <td>181</td>    </tr>    <tr>      <td>2023-01-19</td>      <td>385</td>      <td>168</td>    </tr>    <tr>      <td>2023-01-20</td>      <td>339</td>      <td>278</td>    </tr>    <tr>      <td>2023-01-21</td>      <td>128</td>      <td>238</td>    </tr>    <tr>      <td>2023-01-22</td>      <td>252</td>      <td>217</td>    </tr>    <tr>      <td>2023-01-23</td>      <td>487</td>      <td>263</td>    </tr>    <tr>      <td>2023-01-24</td>      <td>249</td>      <td>207</td>    </tr>    <tr>      <td>2023-01-25</td>      <td>362</td>      <td>231</td>    </tr>    <tr>      <td>2023-01-26</td>      <td>184</td>      <td>117</td>    </tr>    <tr>      <td>2023-01-27</td>      <td>377</td>      <td>106</td>    </tr>    <tr>      <td>2023-01-28</td>      <td>219</td>      <td>253</td>    </tr>    <tr>      <td>2023-01-29</td>      <td>383</td>      <td>169</td>    </tr>    <tr>      <td>2023-01-30</td>      <td>466</td>      <td>129</td>    </tr>    <tr>      <td>2023-01-31</td>      <td>487</td>      <td>95</td>    </tr>    <tr>      <td>2023-02-01</td>      <td>409</td>      <td>140</td>    </tr>    <tr>      <td>2023-02-02</td>      <td>393</td>      <td>129</td>    </tr>    <tr>      <td>2023-02-03</td>      <td>107</td>      <td>275</td>    </tr>    <tr>      <td>2023-02-04</td>      <td>476</td>      <td>61</td>    </tr>    <tr>      <td>2023-02-05</td>      <td>436</td>      <td>297</td>    </tr>    <tr>      <td>2023-02-06</td>      <td>239</td>      <td>183</td>    </tr>    <tr>      <td>2023-02-07</td>      <td>486</td>      <td>208</td>    </tr>    <tr>      <td>2023-02-08</td>      <td>410</td>      <td>236</td>    </tr>    <tr>      <td>2023-02-09</td>      <td>105</td>      <td>118</td>    </tr>    <tr>      <td>2023-02-10</td>      <td>373</td>      <td>109</td>    </tr>    <tr>      <td>2023-02-11</td>      <td>350</td>      <td>82</td>    </tr>    <tr>      <td>2023-02-12</td>      <td>481</td>      <td>87</td>    </tr>    <tr>      <td>2023-02-13</td>      <td>178</td>      <td>221</td>    </tr>    <tr>      <td>2023-02-14</td>      <td>489</td>      <td>175</td>    </tr>    <tr>      <td>2023-02-15</td>      <td>434</td>      <td>110</td>    </tr>    <tr>      <td>2023-02-16</td>      <td>181</td>      <td>95</td>    </tr>    <tr>      <td>2023-02-17</td>      <td>333</td>      <td>79</td>    </tr>    <tr>      <td>2023-02-18</td>      <td>210</td>      <td>205</td>    </tr>    <tr>      <td>2023-02-19</td>      <td>208</td>      <td>281</td>    </tr>    <tr>      <td>2023-02-20</td>      <td>130</td>      <td>77</td>    </tr>    <tr>      <td>2023-02-21</td>      <td>454</td>      <td>79</td>    </tr>    <tr>      <td>2023-02-22</td>      <td>359</td>      <td>176</td>    </tr>    <tr>      <td>2023-02-23</td>      <td>228</td>      <td>122</td>    </tr>    <tr>      <td>2023-02-24</td>      <td>449</td>      <td>125</td>    </tr>    <tr>      <td>2023-02-25</td>      <td>400</td>      <td>147</td>    </tr>    <tr>      <td>2023-02-26</td>      <td>272</td>      <td>256</td>    </tr>    <tr>      <td>2023-02-27</td>      <td>336</td>      <td>88</td>    </tr>    <tr>      <td>2023-02-28</td>      <td>483</td>      <td>61</td>    </tr>    <tr>      <td>2023-03-01</td>      <td>215</td>      <td>252</td>    </tr>    <tr>      <td>2023-03-02</td>      <td>354</td>      <td>296</td>    </tr>    <tr>      <td>2023-03-03</td>      <td>100</td>      <td>139</td>    </tr>    <tr>      <td>2023-03-04</td>      <td>373</td>      <td>82</td>    </tr>    <tr>      <td>2023-03-05</td>      <td>191</td>      <td>228</td>    </tr>    <tr>      <td>2023-03-06</td>      <td>328</td>      <td>90</td>    </tr>    <tr>      <td>2023-03-07</td>      <td>287</td>      <td>248</td>    </tr>    <tr>      <td>2023-03-08</td>      <td>121</td>      <td>80</td>    </tr>    <tr>      <td>2023-03-09</td>      <td>163</td>      <td>200</td>    </tr>    <tr>      <td>2023-03-10</td>      <td>322</td>      <td>173</td>    </tr>    <tr>      <td>2023-03-11</td>      <td>201</td>      <td>125</td>    </tr>    <tr>      <td>2023-03-12</td>      <td>245</td>      <td>85</td>    </tr>    <tr>      <td>2023-03-13</td>      <td>138</td>      <td>262</td>    </tr>    <tr>      <td>2023-03-14</td>      <td>307</td>      <td>246</td>    </tr>    <tr>      <td>2023-03-15</td>      <td>485</td>      <td>113</td>    </tr>    <tr>      <td>2023-03-16</td>      <td>243</td>      <td>54</td>    </tr>    <tr>      <td>2023-03-17</td>      <td>314</td>      <td>227</td>    </tr>    <tr>      <td>2023-03-18</td>      <td>337</td>      <td>166</td>    </tr>    <tr>      <td>2023-03-19</td>      <td>117</td>      <td>207</td>    </tr>    <tr>      <td>2023-03-20</td>      <td>336</td>      <td>241</td>    </tr>    <tr>      <td>2023-03-21</td>      <td>214</td>      <td>111</td>    </tr>    <tr>      <td>2023-03-22</td>      <td>275</td>      <td>141</td>    </tr>    <tr>      <td>2023-03-23</td>      <td>294</td>      <td>161</td>    </tr>    <tr>      <td>2023-03-24</td>      <td>367</td>      <td>261</td>    </tr>    <tr>      <td>2023-03-25</td>      <td>493</td>      <td>154</td>    </tr>    <tr>      <td>2023-03-26</td>      <td>396</td>      <td>140</td>    </tr>    <tr>      <td>2023-03-27</td>      <td>147</td>      <td>76</td>    </tr>    <tr>      <td>2023-03-28</td>      <td>360</td>      <td>123</td>    </tr>    <tr>      <td>2023-03-29</td>      <td>494</td>      <td>228</td>    </tr>    <tr>      <td>2023-03-30</td>      <td>354</td>      <td>273</td>    </tr>    <tr>      <td>2023-03-31</td>      <td>234</td>      <td>144</td>    </tr>    <tr>      <td>2023-04-01</td>      <td>474</td>      <td>67</td>    </tr>    <tr>      <td>2023-04-02</td>      <td>428</td>      <td>249</td>    </tr>    <tr>      <td>2023-04-03</td>      <td>492</td>      <td>106</td>    </tr>    <tr>      <td>2023-04-04</td>      <td>300</td>      <td>293</td>    </tr>    <tr>      <td>2023-04-05</td>      <td>329</td>      <td>85</td>    </tr>    <tr>      <td>2023-04-06</td>      <td>118</td>      <td>251</td>    </tr>    <tr>      <td>2023-04-07</td>      <td>102</td>      <td>270</td>    </tr>    <tr>      <td>2023-04-08</td>      <td>297</td>      <td>97</td>    </tr>    <tr>      <td>2023-04-09</td>      <td>321</td>      <td>98</td>    </tr>    <tr>      <td>2023-04-10</td>      <td>329</td>      <td>169</td>    </tr>  </tbody></table>
                            </div>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="10" style="display: none;">
                        
                        <div class="ridimensionamento col-md-12 col-sm-12 " style="align-items: center;">
                            <div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.34.0.min.js"></script>                <div id="9c9fbf0d-21ec-46b7-b9de-5222f7f6f88e" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("9c9fbf0d-21ec-46b7-b9de-5222f7f6f88e")) {                    Plotly.newPlot(                        "9c9fbf0d-21ec-46b7-b9de-5222f7f6f88e",                        [{"line":{"color":"#00379f","width":1},"mode":"lines","name":"Tangent Function","x":[0.0,0.20408163265306123,0.40816326530612246,0.6122448979591837,0.8163265306122449,1.0204081632653061,1.2244897959183674,1.4285714285714286,1.6326530612244898,1.836734693877551,2.0408163265306123,2.2448979591836737,2.4489795918367347,2.6530612244897958,2.857142857142857,3.0612244897959187,3.2653061224489797,3.4693877551020407,3.673469387755102,3.8775510204081636,4.081632653061225,4.285714285714286,4.4897959183673475,4.6938775510204085,4.8979591836734695,5.1020408163265305,5.3061224489795915,5.510204081632653,5.714285714285714,5.918367346938775,6.122448979591837,6.326530612244898,6.530612244897959,6.73469387755102,6.938775510204081,7.142857142857143,7.346938775510204,7.551020408163265,7.755102040816327,7.959183673469388,8.16326530612245,8.36734693877551,8.571428571428571,8.775510204081632,8.979591836734695,9.183673469387756,9.387755102040817,9.591836734693878,9.795918367346939,10.0],"xaxis":"x","y":[0.0,0.20696293040348496,0.4324492422654186,0.7022656216918376,1.0638519311872643,1.629621529181912,2.7712460816384477,6.983645350820511,-16.14576432495404,-3.6712028473918292,-1.9685385892737552,-1.2516395418940538,-0.8297386363657815,-0.5315032381635652,-0.2923782690447124,-0.0805416457938046,0.12434850262821834,0.34006313829766327,0.5884408054007004,0.905705468918764,1.369349477988887,2.199724371607779,4.418059067175888,54.014509272890784,-5.326796956385151,-2.4351757352982686,-1.4815332322595194,-0.9754694577948535,-0.6394171462175328,-0.38191345226579276,-0.1621350546679556,0.04337247142497885,0.25260289010152154,0.484917007363349,0.7690629790182174,1.1607852238042298,1.800235962369831,3.1991419520736097,10.08032885160561,-9.470425892548851,-3.129519651402599,-1.7737248127373362,-1.146051705067677,-0.759049627158157,-0.4771316376497669,-0.24588765492908585,-0.03703978365443798,0.16863044897014406,0.38917570966419723,0.6483608274590866],"yaxis":"y","type":"scatter"}],                        {"template":{"layout":{"colorway":["#00379f","#007eff","#7bd200","#35009f","#0174af","#db5700","#bbd64a","#a9a3d0","#007eff","#7bd200","#db5700","#ffc000","#403152","#bfbfbf","#00b050","#cc66cd","#00379f","#00b0f0","#92cddc"],"font":{"family":"Arial"}}},"title":{"text":"","x":0.5},"xaxis":{"title":{"text":"X Axis"},"tickmode":"array"},"legend":{"x":0.5,"y":1.15,"xanchor":"center","yanchor":"top","orientation":"h"},"yaxis":{"title":{"text":"Y Axis"}},"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)","plot_bgcolor":"rgba(0,0,0,0)","showlegend":true,"annotations":[{"align":"center","font":{"color":"gray","size":10},"showarrow":false,"text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yanchor":"top","yref":"paper"}]},                        {"responsive": true}                    )                };                            </script>        </div>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="11" style="display: none;">
                        
                        <div class=" graph col-sm-12 col-md-12" style="width:100%">
                            <div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.34.0.min.js"></script>                <div id="5b86ac96-0e13-4135-822f-9f24ce25ffce" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("5b86ac96-0e13-4135-822f-9f24ce25ffce")) {                    Plotly.newPlot(                        "5b86ac96-0e13-4135-822f-9f24ce25ffce",                        [{"line":{"color":"#00379f","width":1},"mode":"lines","name":"Sine Function","x":[0.0,0.20408163265306123,0.40816326530612246,0.6122448979591837,0.8163265306122449,1.0204081632653061,1.2244897959183674,1.4285714285714286,1.6326530612244898,1.836734693877551,2.0408163265306123,2.2448979591836737,2.4489795918367347,2.6530612244897958,2.857142857142857,3.0612244897959187,3.2653061224489797,3.4693877551020407,3.673469387755102,3.8775510204081636,4.081632653061225,4.285714285714286,4.4897959183673475,4.6938775510204085,4.8979591836734695,5.1020408163265305,5.3061224489795915,5.510204081632653,5.714285714285714,5.918367346938775,6.122448979591837,6.326530612244898,6.530612244897959,6.73469387755102,6.938775510204081,7.142857142857143,7.346938775510204,7.551020408163265,7.755102040816327,7.959183673469388,8.16326530612245,8.36734693877551,8.571428571428571,8.775510204081632,8.979591836734695,9.183673469387756,9.387755102040817,9.591836734693878,9.795918367346939,10.0],"xaxis":"x","y":[0.0,0.20266793654820095,0.39692414892492234,0.5747060412161792,0.7286347834693504,0.8523215697196184,0.9406327851124867,0.9899030763721239,0.9980874821347183,0.9648463089837632,0.8915592304110037,0.7812680235262638,0.6385503202266021,0.469329612777201,0.28062939951435684,0.0802816748428135,-0.12339813736217871,-0.3219563150726187,-0.5071517094845144,-0.6712977935519321,-0.8075816909683364,-0.9103469443107827,-0.9753282860670456,-0.9998286683840896,-0.9828312039256306,-0.9250413717382029,-0.8288577363730427,-0.6982723955653996,-0.5387052883861563,-0.3567792408989381,-0.16004508604325057,0.04333173336868346,0.2449100710119793,0.4363234264718193,0.6096271964908323,0.7576284153927202,0.8741842988197335,0.9544571997387519,0.9951153947776636,0.9944713672636168,0.9525518475314604,0.8710967034823207,0.7534867274396376,0.6046033165061543,0.4306258703827373,0.23877531564403087,0.03701440148506237,-0.1662827938487564,-0.3626784288265488,-0.5440211108893698],"yaxis":"y","type":"scatter"},{"line":{"color":"#007eff","width":1},"mode":"lines","name":"Cosine Function","x":[0.0,0.20408163265306123,0.40816326530612246,0.6122448979591837,0.8163265306122449,1.0204081632653061,1.2244897959183674,1.4285714285714286,1.6326530612244898,1.836734693877551,2.0408163265306123,2.2448979591836737,2.4489795918367347,2.6530612244897958,2.857142857142857,3.0612244897959187,3.2653061224489797,3.4693877551020407,3.673469387755102,3.8775510204081636,4.081632653061225,4.285714285714286,4.4897959183673475,4.6938775510204085,4.8979591836734695,5.1020408163265305,5.3061224489795915,5.510204081632653,5.714285714285714,5.918367346938775,6.122448979591837,6.326530612244898,6.530612244897959,6.73469387755102,6.938775510204081,7.142857142857143,7.346938775510204,7.551020408163265,7.755102040816327,7.959183673469388,8.16326530612245,8.36734693877551,8.571428571428571,8.775510204081632,8.979591836734695,9.183673469387756,9.387755102040817,9.591836734693878,9.795918367346939,10.0],"xaxis":"x","y":[1.0,0.9792475210564969,0.9178514149905888,0.8183599245989673,0.6849024400004521,0.5230181084730104,0.33942593237925484,0.14174589725634046,-0.061817295362854206,-0.262814763741325,-0.4529041164186286,-0.6241957028171256,-0.7695800728569471,-0.883023054382162,-0.95981620122199,-0.996772217050833,-0.9923572439880433,-0.9467545253046645,-0.8618567999191831,-0.7411877443484259,-0.5897557226621226,-0.41384591454310704,-0.22075944916926946,-0.018510372154503518,0.18450697707700792,0.37986637199507933,0.5594594291408052,0.7158321462405541,0.842494280256423,0.9341887246502055,0.9871097053688656,0.9990607393363355,0.9695457993910898,0.8997899018725932,0.7926882623697213,0.6526861299196696,0.48559428713386943,0.29834787391040735,0.09871854474461515,-0.10500809346346798,-0.30437637517455507,-0.4911115282522227,-0.6574631180319587,-0.7965267287855184,-0.9025305312049615,-0.9710748419350043,-0.9993147322454036,-0.9860781066780927,-0.931914350819809,-0.8390715290764524],"yaxis":"y","type":"scatter"}],                        {"template":{"layout":{"colorway":["#00379f","#007eff","#7bd200","#35009f","#0174af","#db5700","#bbd64a","#a9a3d0","#007eff","#7bd200","#db5700","#ffc000","#403152","#bfbfbf","#00b050","#cc66cd","#00379f","#00b0f0","#92cddc"],"font":{"family":"Arial"}}},"title":{"text":"","x":0.5},"xaxis":{"title":{"text":"X Axis"},"tickmode":"array"},"legend":{"x":0.5,"y":1.15,"xanchor":"center","yanchor":"top","orientation":"h"},"yaxis":{"title":{"text":"Y Axis"}},"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)","plot_bgcolor":"rgba(0,0,0,0)","showlegend":true,"annotations":[{"align":"center","font":{"color":"gray","size":10},"showarrow":false,"text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yanchor":"top","yref":"paper"}]},                        {"responsive": true}                    )                };                            </script>        </div>
                        </div>
                        <div class="download">
                            <button onclick="downloadCSV('11')">Download</button>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>

    <!-- page -->
    



    <!-- Home -->
    
        <div id="abcde" class="page">
        <h2>Page One</h2>
        <div id="content-page-abcde">
                <div class="content-row" id="content-row-abcde">
                    
                    <div class="row" id="id-content-5" style="display: block;">
                        
                        <div class=" graph col-sm-12 col-md-12" style="width:100%">
                            <div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-2.34.0.min.js"></script>                <div id="5db4ea32-f59e-4d68-b61e-da34e1f36096" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("5db4ea32-f59e-4d68-b61e-da34e1f36096")) {                    Plotly.newPlot(                        "5db4ea32-f59e-4d68-b61e-da34e1f36096",                        [{"line":{"color":"#00379f","width":1},"mode":"lines","name":"Sine Function","x":[0.0,0.20408163265306123,0.40816326530612246,0.6122448979591837,0.8163265306122449,1.0204081632653061,1.2244897959183674,1.4285714285714286,1.6326530612244898,1.836734693877551,2.0408163265306123,2.2448979591836737,2.4489795918367347,2.6530612244897958,2.857142857142857,3.0612244897959187,3.2653061224489797,3.4693877551020407,3.673469387755102,3.8775510204081636,4.081632653061225,4.285714285714286,4.4897959183673475,4.6938775510204085,4.8979591836734695,5.1020408163265305,5.3061224489795915,5.510204081632653,5.714285714285714,5.918367346938775,6.122448979591837,6.326530612244898,6.530612244897959,6.73469387755102,6.938775510204081,7.142857142857143,7.346938775510204,7.551020408163265,7.755102040816327,7.959183673469388,8.16326530612245,8.36734693877551,8.571428571428571,8.775510204081632,8.979591836734695,9.183673469387756,9.387755102040817,9.591836734693878,9.795918367346939,10.0],"xaxis":"x","y":[0.0,0.20266793654820095,0.39692414892492234,0.5747060412161792,0.7286347834693504,0.8523215697196184,0.9406327851124867,0.9899030763721239,0.9980874821347183,0.9648463089837632,0.8915592304110037,0.7812680235262638,0.6385503202266021,0.469329612777201,0.28062939951435684,0.0802816748428135,-0.12339813736217871,-0.3219563150726187,-0.5071517094845144,-0.6712977935519321,-0.8075816909683364,-0.9103469443107827,-0.9753282860670456,-0.9998286683840896,-0.9828312039256306,-0.9250413717382029,-0.8288577363730427,-0.6982723955653996,-0.5387052883861563,-0.3567792408989381,-0.16004508604325057,0.04333173336868346,0.2449100710119793,0.4363234264718193,0.6096271964908323,0.7576284153927202,0.8741842988197335,0.9544571997387519,0.9951153947776636,0.9944713672636168,0.9525518475314604,0.8710967034823207,0.7534867274396376,0.6046033165061543,0.4306258703827373,0.23877531564403087,0.03701440148506237,-0.1662827938487564,-0.3626784288265488,-0.5440211108893698],"yaxis":"y","type":"scatter"},{"line":{"color":"#007eff","width":1},"mode":"lines","name":"Cosine Function","x":[0.0,0.20408163265306123,0.40816326530612246,0.6122448979591837,0.8163265306122449,1.0204081632653061,1.2244897959183674,1.4285714285714286,1.6326530612244898,1.836734693877551,2.0408163265306123,2.2448979591836737,2.4489795918367347,2.6530612244897958,2.857142857142857,3.0612244897959187,3.2653061224489797,3.4693877551020407,3.673469387755102,3.8775510204081636,4.081632653061225,4.285714285714286,4.4897959183673475,4.6938775510204085,4.8979591836734695,5.1020408163265305,5.3061224489795915,5.510204081632653,5.714285714285714,5.918367346938775,6.122448979591837,6.326530612244898,6.530612244897959,6.73469387755102,6.938775510204081,7.142857142857143,7.346938775510204,7.551020408163265,7.755102040816327,7.959183673469388,8.16326530612245,8.36734693877551,8.571428571428571,8.775510204081632,8.979591836734695,9.183673469387756,9.387755102040817,9.591836734693878,9.795918367346939,10.0],"xaxis":"x","y":[1.0,0.9792475210564969,0.9178514149905888,0.8183599245989673,0.6849024400004521,0.5230181084730104,0.33942593237925484,0.14174589725634046,-0.061817295362854206,-0.262814763741325,-0.4529041164186286,-0.6241957028171256,-0.7695800728569471,-0.883023054382162,-0.95981620122199,-0.996772217050833,-0.9923572439880433,-0.9467545253046645,-0.8618567999191831,-0.7411877443484259,-0.5897557226621226,-0.41384591454310704,-0.22075944916926946,-0.018510372154503518,0.18450697707700792,0.37986637199507933,0.5594594291408052,0.7158321462405541,0.842494280256423,0.9341887246502055,0.9871097053688656,0.9990607393363355,0.9695457993910898,0.8997899018725932,0.7926882623697213,0.6526861299196696,0.48559428713386943,0.29834787391040735,0.09871854474461515,-0.10500809346346798,-0.30437637517455507,-0.4911115282522227,-0.6574631180319587,-0.7965267287855184,-0.9025305312049615,-0.9710748419350043,-0.9993147322454036,-0.9860781066780927,-0.931914350819809,-0.8390715290764524],"yaxis":"y","type":"scatter"}],                        {"template":{"layout":{"colorway":["#00379f","#007eff","#7bd200","#35009f","#0174af","#db5700","#bbd64a","#a9a3d0","#007eff","#7bd200","#db5700","#ffc000","#403152","#bfbfbf","#00b050","#cc66cd","#00379f","#00b0f0","#92cddc"],"font":{"family":"Arial"}}},"title":{"text":"","x":0.5},"xaxis":{"title":{"text":"X Axis"},"tickmode":"array"},"legend":{"x":0.5,"y":1.15,"xanchor":"center","yanchor":"top","orientation":"h"},"yaxis":{"title":{"text":"Y Axis"}},"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)","plot_bgcolor":"rgba(0,0,0,0)","showlegend":true,"annotations":[{"align":"center","font":{"color":"gray","size":10},"showarrow":false,"text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend.","x":0.5,"xanchor":"center","xref":"paper","y":-0.2,"yanchor":"top","yref":"paper"}]},                        {"responsive": true}                    )                };                            </script>        </div>
                        </div>
                        <div class="download">
                            <button onclick="downloadCSV('id-content-5')">Download</button>
                        </div>
                        
                    </div>
                    
                    <div class="row" id="id-content-8" style="display: block;">
                        
                        <div class="col-sm-12 col-md-12 table-large">
                            <div class="table-container table-sm table-scrollable" border="0" index="false"
                                 style="text-align: justify;    overflow-x: hidden; ">
                                <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>x</th>      <th>y</th>      <th>z</th>    </tr>  </thead>  <tbody>    <tr>      <td>0.000000</td>      <td>0.000000</td>      <td>1.000000</td>    </tr>    <tr>      <td>0.204082</td>      <td>0.202668</td>      <td>0.979248</td>    </tr>    <tr>      <td>0.408163</td>      <td>0.396924</td>      <td>0.917851</td>    </tr>    <tr>      <td>0.612245</td>      <td>0.574706</td>      <td>0.818360</td>    </tr>    <tr>      <td>0.816327</td>      <td>0.728635</td>      <td>0.684902</td>    </tr>    <tr>      <td>1.020408</td>      <td>0.852322</td>      <td>0.523018</td>    </tr>    <tr>      <td>1.224490</td>      <td>0.940633</td>      <td>0.339426</td>    </tr>    <tr>      <td>1.428571</td>      <td>0.989903</td>      <td>0.141746</td>    </tr>    <tr>      <td>1.632653</td>      <td>0.998087</td>      <td>-0.061817</td>    </tr>    <tr>      <td>1.836735</td>      <td>0.964846</td>      <td>-0.262815</td>    </tr>    <tr>      <td>2.040816</td>      <td>0.891559</td>      <td>-0.452904</td>    </tr>    <tr>      <td>2.244898</td>      <td>0.781268</td>      <td>-0.624196</td>    </tr>    <tr>      <td>2.448980</td>      <td>0.638550</td>      <td>-0.769580</td>    </tr>    <tr>      <td>2.653061</td>      <td>0.469330</td>      <td>-0.883023</td>    </tr>    <tr>      <td>2.857143</td>      <td>0.280629</td>      <td>-0.959816</td>    </tr>    <tr>      <td>3.061224</td>      <td>0.080282</td>      <td>-0.996772</td>    </tr>    <tr>      <td>3.265306</td>      <td>-0.123398</td>      <td>-0.992357</td>    </tr>    <tr>      <td>3.469388</td>      <td>-0.321956</td>      <td>-0.946755</td>    </tr>    <tr>      <td>3.673469</td>      <td>-0.507152</td>      <td>-0.861857</td>    </tr>    <tr>      <td>3.877551</td>      <td>-0.671298</td>      <td>-0.741188</td>    </tr>    <tr>      <td>4.081633</td>      <td>-0.807582</td>      <td>-0.589756</td>    </tr>    <tr>      <td>4.285714</td>      <td>-0.910347</td>      <td>-0.413846</td>    </tr>    <tr>      <td>4.489796</td>      <td>-0.975328</td>      <td>-0.220759</td>    </tr>    <tr>      <td>4.693878</td>      <td>-0.999829</td>      <td>-0.018510</td>    </tr>    <tr>      <td>4.897959</td>      <td>-0.982831</td>      <td>0.184507</td>    </tr>    <tr>      <td>5.102041</td>      <td>-0.925041</td>      <td>0.379866</td>    </tr>    <tr>      <td>5.306122</td>      <td>-0.828858</td>      <td>0.559459</td>    </tr>    <tr>      <td>5.510204</td>      <td>-0.698272</td>      <td>0.715832</td>    </tr>    <tr>      <td>5.714286</td>      <td>-0.538705</td>      <td>0.842494</td>    </tr>    <tr>      <td>5.918367</td>      <td>-0.356779</td>      <td>0.934189</td>    </tr>    <tr>      <td>6.122449</td>      <td>-0.160045</td>      <td>0.987110</td>    </tr>    <tr>      <td>6.326531</td>      <td>0.043332</td>      <td>0.999061</td>    </tr>    <tr>      <td>6.530612</td>      <td>0.244910</td>      <td>0.969546</td>    </tr>    <tr>      <td>6.734694</td>      <td>0.436323</td>      <td>0.899790</td>    </tr>    <tr>      <td>6.938776</td>      <td>0.609627</td>      <td>0.792688</td>    </tr>    <tr>      <td>7.142857</td>      <td>0.757628</td>      <td>0.652686</td>    </tr>    <tr>      <td>7.346939</td>      <td>0.874184</td>      <td>0.485594</td>    </tr>    <tr>      <td>7.551020</td>      <td>0.954457</td>      <td>0.298348</td>    </tr>    <tr>      <td>7.755102</td>      <td>0.995115</td>      <td>0.098719</td>    </tr>    <tr>      <td>7.959184</td>      <td>0.994471</td>      <td>-0.105008</td>    </tr>    <tr>      <td>8.163265</td>      <td>0.952552</td>      <td>-0.304376</td>    </tr>    <tr>      <td>8.367347</td>      <td>0.871097</td>      <td>-0.491112</td>    </tr>    <tr>      <td>8.571429</td>      <td>0.753487</td>      <td>-0.657463</td>    </tr>    <tr>      <td>8.775510</td>      <td>0.604603</td>      <td>-0.796527</td>    </tr>    <tr>      <td>8.979592</td>      <td>0.430626</td>      <td>-0.902531</td>    </tr>    <tr>      <td>9.183673</td>      <td>0.238775</td>      <td>-0.971075</td>    </tr>    <tr>      <td>9.387755</td>      <td>0.037014</td>      <td>-0.999315</td>    </tr>    <tr>      <td>9.591837</td>      <td>-0.166283</td>      <td>-0.986078</td>    </tr>    <tr>      <td>9.795918</td>      <td>-0.362678</td>      <td>-0.931914</td>    </tr>    <tr>      <td>10.000000</td>      <td>-0.544021</td>      <td>-0.839072</td>    </tr>  </tbody></table>
                            </div>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>

    <!-- footer -->
    



    <!-- Home -->
    
        <div id="abcdef" class="page">
        <h2>Page Two</h2>
        <div id="content-page-abcdef">
                <div class="content-row" id="content-row-abcdef">
                    
                    <div class="row" id="" style="display: ;">
                        
                        <div class="col-md-7 col-sm-12 text3">
                            <h2><h3> Lorem sed iaculis leo dictum. </h3></h2>
                            <p><p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, mollis quis fermentum at, lacinia vitae risus. Vestibulum suscipit fermentum mi, a feugiat enim. Ut a mattis augue, placerat ornare magna. Sed varius pharetra augue. Phasellus id mollis felis, vel vestibulum felis. Aliquam massa elit, faucibus sed ultrices vel, eleifend tristique nulla. Curabitur at massa sit amet ligula aliquam tincidunt. Praesent rhoncus pulvinar molestie. Donec molestie erat aliquet diam viverra, sed iaculis leo dictum. Phasellus consequat felis sit amet pulvinar bibendum. Aliquam fermentum nulla mi, quis ultricies lacus mollis vel. Phasellus sollicitudin commodo est, sit amet tristique leo feugiat vitae. Integer odio felis, consequat ut venenatis sit amet, accumsan eu metus. Curabitur id risus et elit tempor dapibus. Donec molestie sodales mattis. </p></p>
                        </div>
                        <div class="img2 col-md-5 col-sm-12 ">
                            <img src="https://raw.githubusercontent.com/fr-cm/interfaccia/main/Tutorial/img/gif/type_page.gif" alt="Image" style="max-width: 100%; height: auto;">
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>

    <!-- footer -->
    



    <!-- Home -->
    
        <div id="note" class="page">
        <h2>Repositories</h2>
        <div id="content-page-note">
                <div class="content-row" id="content-row-note">
                    
                    <div class="row" id="" style="display: ;">
                        
                        <div class="html" >
                            <div col-sm-12' style=' display: flex; justify-content: center; align-items: center; flex-direction: column; margin: 20px; text-align: center;'>
<p><br>link for:<br><br><strong><a href='https://github.com/fr-cm/interfaccia'>Repository</a></strong><br><br><strong><a href='https://github.com/fr-cm/interfaccia'>Tutorial</a></strong><br></p></div>
                        </div>
                        
                    </div>
                    
                </div>
            </div>
        </div>

    <!-- footer -->
    



    <!-- Home -->
    
        <div id="footer" class="footer"
         style="display: flex; background-color: #e7e8f2; justify-content: center; align-items: center; margin-top:3rem ; margin-left: 4rem; margin-right:4rem">
        <div class="row align-items-center" style="text-align: center; width: 100%; font-size: 10px;">
            <div class="footer-section" style="width: 100%;">
                <div class="col-sm-12">
                    <p style="color: #4a4a4a; text-align: center; font-size: 10px;">
                        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean volutpat ipsum dictum placerat eleifend. Vestibulum lectus libero, </p>

                    </p>
                </div>
            </div>
        </div>
    </div>

    




<footer class="footer_fix" style="text-align: center;argin-top:1.6rem">
    <p class="footer-text" style="color: gray; font-size: x-small; justify-content: center; margin-top: 10px;">
        <strong><a href="https://github.com/fr-cm/interfaccia">created by interfaccia of F.CAMASSA</a></strong>

    </p>
</footer>

<!-- Javascript  -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Forces plotly graph resize given the presence of a bug
        const graphSelector = document.querySelector('.form-select');
        if (graphSelector) {
            const initialValue = graphSelector.value;
            updateDisplay(graphSelector.closest('.page-menu').id, initialValue);
        }

        // listener for navbar
        document.querySelectorAll('.navbar-nav .nav-link').forEach(function(element) {
            element.addEventListener('click', function(event) {
                var subMenu = this.nextElementSibling;
                if (subMenu && subMenu.classList.contains('dropdown-menu')) {
                    // closing delay sub-menu
                    event.preventDefault();
                    event.stopPropagation();
                    // hide sub-menu
                    subMenu.classList.toggle('show');
                } else {
                    // closing menu
                    var navbarCollapse = document.querySelector('.navbar-collapse');
                    var bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                        toggle: false
                    });
                    bsCollapse.hide();
                }
            });
        });

        // listener sub-menu
        document.querySelectorAll('.dropdown-menu .dropdown-item').forEach(function(element) {
            element.addEventListener('click', function() {
                // closing menu
                var navbarCollapse = document.querySelector('.navbar-collapse');
                var bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                    toggle: false
                });
                bsCollapse.hide();
            });
        });

        // listener tab Bootstrap
        document.addEventListener('shown.bs.tab', function (event) {
            var activePane = document.querySelector('.tab-pane.active');
            var plotElements = activePane.querySelectorAll('.js-plotly-plot');
            plotElements.forEach(function(plotElement) {
                Plotly.Plots.resize(plotElement);
            });
        });
    });

    function updateDisplay(pageId, selectedId) {
        // PupdateDisplay for dropdown menu of page_menu
        let contentRow = document.getElementById('content-row-' + pageId);

        const allContent = contentRow.querySelectorAll('.row');

        // hide content
        allContent.forEach(function(content) {
            content.style.display = 'none';
        });

        // show only selected content
        const selectedContent = document.getElementById(selectedId);
        if (selectedContent) {
            selectedContent.style.display = 'flex';  // Usa flex per mantenere l'allineamento

            // delay content
            setTimeout(function() {
                const plotElements = selectedContent.querySelectorAll('.js-plotly-plot');
                plotElements.forEach(function(plotElement) {
                    Plotly.Plots.resize(plotElement);
                });
            }, 100); // Adjust delay as needed
        }
    }

    // function to convert dataplot in CSV
    function plotlyToCSV(plotData) {
        let csv = 'x,y\n';
        plotData.forEach(function(trace) {
            for (let i = 0; i < trace.x.length; i++) {
                csv += trace.x[i] + ',' + trace.y[i] + '\n';
            }
        });
        return csv;
    }

    // function cvs download
    function downloadCSV(plotId) {
        // take ID plot
        let plot = document.getElementById(plotId).querySelector('.js-plotly-plot');
        if (plot) {
            let plotData = plot.data;

            // convert data in CSV
            let csv = plotlyToCSV(plotData);

            // blob creation
            let blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            let url = URL.createObjectURL(blob);

            // download link creation
            let a = document.createElement('a');
            a.href = url;
            a.download = plotId + '_data.csv';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        } else {
            console.error('Plot not found for ID:', plotId);
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        // click listener
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();

                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);

                const offset = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - offset;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            });
        });
    });
</script>

</body>
</html>
