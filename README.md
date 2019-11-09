# Veracode SDK / API 

This is a work in progress.  It currently only supports the [Results API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/WgCXPStuSb3isrDrHlmV9Q) and partial support for the [Upload API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/qUW0fV37Fd~NHav8afNqMg). There is also a top level helper class `Application`, 
this can be instantiated with an application name which exposes properties that will zazy load data from the corresponding API. 

New modules will be added as time permits.

Tests and a proper setup comming soon. For now read the docs, source, or use your tab key 🤪.

## Install

I will add a `setup.py` shortly.  Currently you can do the following to test.

```bash
$ git clone https://github.com/chuckorde/veracode-SDK.git 
$ cd veracode-SDK
$ export PYTHONPATH=${PYTHONPATH}:$(pwd)
```

## Configuration
```bash
$ python3 -m veracode.configure
```

## Usage

### Top level classes

```python
In [1]: from veracode.application import Application                            

In [2]: app = Application('WebGoat')                                            

In [3]: summary = app.summary                                                   

In [4]: summary                                                                 
Out[4]: <veracode.SDK.results.SummaryReport at 0x109604be0>

In [5]: details = app.details                                                   

In [6]: details                                                                 
Out[6]: <veracode.SDK.results.DetailedReport at 0x1096f10f0>

In [7]: app.details.first_build_submitted_date                                  
Out[7]: datetime.date(2018, 10, 23)
```

### Direct SDK access
Returns a python object with a one-to-one mapping to the returned XML

```python
In [1]: from veracode import SDK       
    
In [2]: result = SDK.results.SummaryReport(build_id=2412498) # use a valid id for your app.
    
In [3]: print(result.flaws_not_mitigated)                                                            
161

```

### Direct API access
Returns a constom response object with properties `data`: returned XML and `status_code`: server response code.  The full response is also avialable.

```python
In [1]: from veracode import API                                                

In [2]: builds = API.results.GetAppBuilds.get()                                 

In [3]: builds                                                                  
Out[3]: <veracode.API.core.REST.response at 0x107f57c88>

In [4]: builds.status_code                                                      
Out[4]: 200

In [5]: builds.data[:20]                                                        
Out[5]: '<?xml version="1.0" '

```

<!DOCTYPE html>
<meta charset="utf-8">
<style>
    svg {padding: 30px}
    
.node circle {
  fill: #999;
}

.node text {
  font: 12px sans-serif;
}

.node--internal circle {
  fill: #555;
}

.node--internal text {
  text-shadow: 0 1px 0 #fff, 0 -1px 0 #fff, 1px 0 0 #fff, -1px 0 0 #fff;
}

.link {
  fill: none;
  stroke: #555;
  stroke-opacity: 0.4;
  stroke-width: 1.5px;
}

form {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  position: absolute;
  left: 10px;
  top: 10px;
    display: none;
}

label {
  display: block;
}

</style>
<form>
  <label><input type="radio" name="mode" value="cluster" checked> Dendrogram</label>
  <label><input type="radio" name="mode" value="tree"> Tree</label>
</form>
<svg width="1000" height="6000"></svg>
<script src="//d3js.org/d3.v4.min.js"></script>
<script>

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height"),
    g = svg.append("g").attr("transform", "translate(40,0)");

var tree = d3.tree()
    .size([height - 100, width - 160]);

var cluster = d3.cluster()
    .size([height, width - 200]);

var stratify = d3.stratify()
    .parentId(function(d) { return d.id.substring(0, d.id.lastIndexOf("#")); });

d3.csv("flare.csv", function(error, data) {
  if (error) throw error;

  var root = stratify(data)
      .sort(function(a, b) { return (a.height - b.height) || a.id.localeCompare(b.id); });

  cluster(root);

  var link = g.selectAll(".link")
      .data(root.descendants().slice(1))
    .enter().append("path")
      .attr("class", "link")
      .attr("d", diagonal);

  var node = g.selectAll(".node")
      .data(root.descendants())
    .enter().append("g")
      .attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
      .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

  node.append("circle")
      .attr("r", 2.5);

  node.append("text")
      .attr("dy", 3)
      .attr("x", function(d) { return d.children ? -8 : 8; })
      .style("text-anchor", function(d) { return d.children ? "end" : "start"; })
      .text(function(d) { return d.id.substring(d.id.lastIndexOf("#") + 1); });

  d3.selectAll("input")
      .on("change", changed);

    /*
  var timeout = setTimeout(function() {
    d3.select("input[value=\"tree\"]")
        .property("checked", true)
        .dispatch("change");
  }, 1000);
  */

  function changed() {
    timeout = clearTimeout(timeout);
    (this.value === "tree" ? tree : cluster)(root);
    var t = d3.transition().duration(750);
    node.transition(t).attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });
    link.transition(t).attr("d", diagonal);
  }
});

function diagonal(d) {
  return "M" + d.y + "," + d.x
      + "C" + (d.parent.y + 100) + "," + d.x
      + " " + (d.parent.y + 100) + "," + d.parent.x
      + " " + d.parent.y + "," + d.parent.x;
}

</script>