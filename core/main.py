from core import local_constants, spread_service

srv = spread_service.SpreadService()
sheet = srv.get_sheet()
result = sheet.values().get(spreadsheetId=local_constants.SPREADSHEET_ID,
                            range='Динамика!H10:H12').execute()
print(sheet)
