describe('helpers functions covering total payment, tip calculation', () => {
    beforeEach(() => {
        // Initiate payment values. 
        billAmtInput.value = 50;
        tipAmtInput.value = 5;
        submitPaymentInfo();
    });

    it('validate the tip amount', () =>{
        // $5 (tip amount) / $50 (bill amount) = 5% tip = $5 tip amount.
        expect(sumPaymentTotal('tipAmt')).toEqual(5);

        // try another case $60 / $300 = 20% tip = $60. 
        billAmtInput.value = 300;
        tipAmtInput.value = 60;
      
        submitPaymentInfo();
        expect(sumPaymentTotal('tipAmt')).toEqual(65);
    });

    it('validate the total bill amount', () =>{
        billAmtInput.value = 300;
        tipAmtInput.value = 60;
        submitPaymentInfo();
        expect(sumPaymentTotal('billAmt')).toEqual(350);
    });

    it('validate the total tip percentage', () =>{
        expect(sumPaymentTotal('tipPercent')).toEqual(10);

        billAmtInput.value = 300;
        tipAmtInput.value = 60;
        submitPaymentInfo();
        expect(sumPaymentTotal('tipPercent')).toEqual(30);
    });

    it('validate the tip percentange on a single tip on calculateTipPercent()', () =>{
        expect(calculateTipPercent(100, 10)).toEqual(10);
        expect(calculateTipPercent(150, 20)).toEqual(13);
    });

    it('validate a new Td element on appendTd(tr, value)', () => {
        let newTd = document.createElement('tr');
        appendTd(newTd, 'test');
        expect(newTd.children.length).toEqual(1);
    });

    it('validate if the delete button gets appended to #serverTable', () =>{
        let newTR = document.createElement('tr');
        appendDeleteBtn(newTR);
        expect(newTR.children.length).toEqual(1);
        expect(newTR.firstChild.innerHTML).toEqual('X');
    });

    afterEach(() =>{
        billAmtInput.value = '';
        tipAmtInput.value = '';
        paymentTbody.innerHTML = '';
        summaryTds[0].innerHTML = '';
        summaryTds[1].innerHTML = '';
        summaryTds[2].innerHTML = '';
        serverTbody.innerHTML = '';
        allPayments = {};
        paymentId = 0;
    })

});

