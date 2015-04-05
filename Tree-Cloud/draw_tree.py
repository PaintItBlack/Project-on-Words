#Open File to write the D3 Graph
output_file = open('d3js_project/treecloud.html', 'w')

output_file.write("""
<!DOCTYPE html>

<meta charset="utf-8">
<style>

.node {
  stroke: #fff;
  stroke-width: 1.5px;
}

.link {
  stroke: #999;
  stroke-opacity: .6;
}

</style>
<body>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script>

var width = 960,
    height = 500;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(30)
    .size([width, height]);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("toptest.json", function(error, graph) {
  force
      .nodes(graph.nodes)
      .links(graph.links)
      .start();

  var link = svg.selectAll(".link")
      .data(graph.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return Math.sqrt(d.value); });

// Create the groups under svg
var gnodes = svg.selectAll('g.gnode')
  .data(graph.nodes)
  .enter()
  .append('g')
  .classed('gnode', true);

// Append the labels to each group
var labels = gnodes.append("text")
  .text(function(d) { return d.name; })
  .attr("fill", function(d) { return color(d.group); })
  .attr("font-size", "20px")
  .attr("font-family", "sans-serif")
  .attr("text-anchor", "middle");

force.on("tick", function() {
  // Update the links
  link.attr("x1", function(d) { return d.source.x; })
    .attr("y1", function(d) { return d.source.y; })
    .attr("x2", function(d) { return d.target.x; })
    .attr("y2", function(d) { return d.target.y; });

  // Translate the groups
  gnodes.attr("transform", function(d) { 
    return 'translate(' + [d.x, d.y] + ')'; 
  });    

});
  
});

</script>""")

output_file.close()
