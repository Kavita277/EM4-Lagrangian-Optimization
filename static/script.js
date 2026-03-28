let barChart = null;

function solve() {
    let objective = document.getElementById("objective").value;
    let constraint = document.getElementById("constraint").value;
    let mode = document.getElementById("mode").value;

    fetch('/solve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ objective, constraint, mode })
    })
    .then(res => res.json())
    .then(data => {

        if (data.solution && data.solution.error) {
            document.getElementById("output").innerHTML = "❌ " + data.solution.error;
            document.getElementById("explanation").innerText = "";
            document.getElementById("plotlyGraph").style.display = "none";
            return;
        }

        let sol = data.solution;

        // OUTPUT DISPLAY
        let output = `<b>✨ Optimal Solution:</b><br>`;
        for (let key in sol) {
            if (key !== "plotly_json") {
                output += `${key} = ${sol[key].toFixed(4)} <br>`;
            }
        }
        document.getElementById("output").innerHTML = output;

        if (sol.plotly_json) {
            document.getElementById("plotlyGraph").style.display = "block";
            let fig = JSON.parse(sol.plotly_json);
            Plotly.newPlot("plotlyGraph", fig.data, fig.layout, {responsive: true});
        } else {
            document.getElementById("plotlyGraph").style.display = "none";
        }

         let explanationText = data.explanation || "⚠️ No explanation generated.";
        document.getElementById("explanation").innerHTML = marked.parse(explanationText);

        if (window.MathJax) {
            MathJax.typesetPromise([document.getElementById("explanation")]).catch(function (err) {
                console.error('MathJax error: ', err.message);
            });
        }

        // DRAW BAR CHART
        drawBarChart(sol);
    })
    .catch(err => {
        document.getElementById("output").innerHTML = "❌ Error connecting to server";
        console.error(err);
    });
}
/* ===============================
   📊 3D BAR CHART FUNCTION (PLOTLY)
================================ */
function drawBarChart(sol) {
    let labels = [];
    let values = [];

    for (let key in sol) {
        if (key !== "Z" && key !== "plotly_json") {
            labels.push(key);
            values.push(sol[key]);
        }
    }

    let traces = [];

    // Create a 3D neon pillar for each variable
    for (let i = 0; i < labels.length; i++) {
        traces.push({
            type: 'scatter3d',
            mode: 'lines+markers',
            x: [labels[i], labels[i]],
            y: [0, 0],             // Keeps them aligned in a single row
            z: [0, values[i]],     // Pillar stretches from 0 to the value
            line: {
                width: 25,         // 🔥 Thick line to simulate a 3D bar
                color: '#00eaff'
            },
            marker: {
                size: 6,
                color: '#ffffff',  // Glowing white tip
                symbol: 'diamond'
            },
            name: labels[i]
        });
    }

    let layout = {
        title: { text: "3D Optimal Variable Pillars", font: { color: 'white', size: 14 } },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        scene: {
            xaxis: { title: 'Variables', color: '#00eaff', gridcolor: 'rgba(255,255,255,0.1)' },
            yaxis: { showticklabels: false, visible: false }, // Hide Y axis for a clean view
            zaxis: { title: 'Value', color: '#00eaff', gridcolor: 'rgba(255,255,255,0.1)' },
            camera: {
                eye: { x: 1.5, y: -1.5, z: 0.5 } // Good default 3D viewing angle
            }
        },
        showlegend: false,
        margin: { l: 0, r: 0, b: 0, t: 40 }
    };

    // Draw the 3D Bar chart!
    Plotly.newPlot("barChart", traces, layout, {responsive: true});
}

        
