describe('Payment tests', () =>{
    beforeEach(() =>{
        billAmtInput.value = 50;
        tipAmtInput.value = 5;
    });

    it('should add a new payment on submitPaymentInfo()', () =>{
        submitPaymentInfo();
        expect(Object.keys(allPayments).length).toEqual(1);
        expect(allPayments['payment1'].billAmt).toEqual('50');
        expect(allPayments['payment1'].tipAmt).toEqual('5');
        expect(allPayments['payment1'].tipPercent).toEqual(10);
    });

    it('should not add a new payment on submitPaymentInfo() if input is empty', () =>{
        billAmtInput.value = '';
        submitPaymentInfo();
        expect(Object.keys(allPayments).length).toEqual(0);
    });

    it('should add payment info to #paymentTable on appendPaymentTable()', () =>{
        let currPayment = createCurPayment();
        allPayments['payment1'] = currPayment;
        appendPaymentTable(currPayment);
        let currP1 = document.querySelectorAll('#paymentTable tbody tr td');

        expect(currP1.length).toEqual(3);
        expect(currP1[0].innerText).toEqual('$50');
        expect(currP1[1].innerText).toEqual('$5');
        expect(currP1[2].innerText).toEqual('10%');

    });

    it('should not accept empty inputs on createCurPayment()', () =>{
        billAmtInput.value = '';
        tipAmtInput.value = '';
        let testCP = createCurPayment();
        expect(testCP).toEqual(undefined);
    });

    afterEach(() =>{
        billAmtInput.value = '';
        tipAmtInput.value = '';
        paymentTbody.innerHTML = '';
        summaryTds[0].innerHTML = '';
        summaryTds[1].innerHTML = '';
        summaryTds[2].innerHTML = '';
        serverTbody.innerHTML = '';
        paymentId = 0;
        allPayments = {};
    });
});