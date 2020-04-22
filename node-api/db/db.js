const recipes = [
    {
        id: 1,
        title: "Aloo Palak",
        ingredients: [
            {
                name: "Potatoes",
                quantity: 2,
                uom: "count"
            },
            {
                name: "Spinach",
                quantity: 9,
                uom: "oz"
            },
            {
                name: "Cumin Seeds",
                quantity: 1,
                uom: "tsp"
            }
        ],
        steps: [
            {
                number: 1,
                description: "Bring cumin seeds to a sizzle in hot oil."
            },
            {
                number: 2,
                description: "Add red chilies, hing and something else."
            }
        ]
    }
]

export default recipes;
