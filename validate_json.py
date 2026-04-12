import json
import os
from pathlib import Path

def validate_json_files():
    """Validate all JSON files in the data directory"""
    data_dir = Path("data")
    json_files = list(data_dir.glob("*.json"))
    
    print("=" * 60)
    print("VALIDACIÓN DE ARCHIVOS JSON")
    print("=" * 60)
    
    results = []
    all_valid = True
    
    for json_file in sorted(json_files):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Count keys/items for summary
            if isinstance(data, dict):
                keys = len(data.keys())
                status = "✓ VÁLIDO"
            elif isinstance(data, list):
                keys = len(data)
                status = "✓ VÁLIDO"
            else:
                keys = 0
                status = "✓ VÁLIDO"
            
            results.append({
                'file': json_file.name,
                'status': status,
                'items': keys,
                'valid': True
            })
            
        except json.JSONDecodeError as e:
            results.append({
                'file': json_file.name,
                'status': f"✗ ERROR: {str(e)}",
                'items': 0,
                'valid': False
            })
            all_valid = False
        except Exception as e:
            results.append({
                'file': json_file.name,
                'status': f"✗ ERROR: {str(e)}",
                'items': 0,
                'valid': False
            })
            all_valid = False
    
    # Print results
    print(f"\nTotal archivos: {len(results)}\n")
    
    for result in results:
        print(f"📄 {result['file']:<25} {result['status']:<20} ({result['items']} elementos)")
    
    print("\n" + "=" * 60)
    if all_valid:
        print("✓ TODOS LOS ARCHIVOS JSON SON VÁLIDOS")
    else:
        print("✗ SE ENCONTRARON ERRORES EN ALGUNOS ARCHIVOS")
    print("=" * 60)
    
    return all_valid

if __name__ == "__main__":
    validate_json_files()
