
describe("Servers test (with setup and tear-down)", function() {
  beforeEach(function () {
    // initialization logic
    serverNameInput.value = 'Alice';
  });

  it('should add a new server to allServers on submitServerInfo()', function () {
    submitServerInfo();
    expect(Object.keys(allServers).length).toEqual(1);
    expect(allServers['server' + serverId].serverName).toEqual('Alice');
  });

  it('should not add a new server to Allservers on submitServerInfo() with an empty input',
    () => {
      serverNameInput.value = '';
      submitServerInfo();
      expect(Object.keys(allServers).length).toEqual(0)
    });

  it('it should update #serverTable on updateServerTable()', () => {
    submitServerInfo();
    let updateServer = document.querySelectorAll('#serverTable tbody tr td');
    expect(updateServer.length).toEqual(3);   // Server Name and Earnings
    expect(updateServer[0].innerText).toEqual('Alice');   // Server Name = 'Alice'
    expect(updateServer[1].innerText).toEqual('$0.00');   // Earnings = '$0.00'
    expect(updateServer[2].innerText).toEqual('X');       // 'X' delete button
  });
  
  afterEach(function() {
    // teardown logic
    allServers = {};
    serverID = 0;
    serverTbody.innerHTML = '';
  }); 
});
