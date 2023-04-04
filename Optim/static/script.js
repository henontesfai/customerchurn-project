async function updatePrediction() {
    const contract = document.querySelector('select[name="contract"]').value;
    const tenure = document.querySelector('input[name="tenure"]').value;
    const monthly_charges = document.querySelector('input[name="monthly_charges"]').value;
    const total_charges = document.querySelector('input[name="total_charges"]').value;

    const response = await fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ contract, tenure, monthly_charges, total_charges })
    });

    if (!response.ok) {
        console.error("Failed to fetch the prediction", response);
        return;
    }

    const data = await response.json();

    const predictionText = document.querySelector('#result');
    if (data.prediction === 1) {
        predictionText.textContent = 'The customer is likely to churn.';
    } else {
        predictionText.textContent = 'The customer is likely to stay.';
    }
}

function predictButtonClick(event) {
    event.preventDefault();
    updatePrediction();
}

document.querySelector('form').addEventListener('submit', predictButtonClick);

document.querySelector('input[name="monthly_charges_number"]').addEventListener('input', () => {
    const input = document.querySelector('input[name="monthly_charges_number"]');
    document.querySelector('input[name="monthly_charges"]').value = input.value;
    updatePrediction();
});

document.querySelector('input[name="monthly_charges_number"]').addEventListener('blur', () => {
    const input = document.querySelector('input[name="monthly_charges_number"]');
    if (input.value < 20) {
        input.value = 20;
    } else if (input.value > 120) {
        input.value = 120;
    }
    document.querySelector('input[name="monthly_charges"]').value = input.value;
    updatePrediction();
});

document.querySelector('input[name="total_charges_number"]').addEventListener('input', () => {
    const input = document.querySelector('input[name="total_charges_number"]');
    document.querySelector('input[name="total_charges"]').value = input.value;
    updatePrediction();
});

document.querySelector('input[name="total_charges_number"]').addEventListener('blur', () => {
    const input = document.querySelector('input[name="total_charges_number"]');
    if (input.value < 20) {
        input.value = 20;
    } else if (input.value > 10000) {
        input.value = 10000;
    }
    document.querySelector('input[name="total_charges"]').value = input.value;
    updatePrediction();
});


