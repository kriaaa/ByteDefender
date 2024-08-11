import pickle
import pefile
import numpy as np
import joblib


def load_model():
    model_path = "model.pkl"
    loaded_model = joblib.load(model_path)
    return loaded_model


def extract_features(file_path):
    pe = pefile.PE(file_path)
   
    extracted_features = {}
   
    # Extract features
    extracted_features['ImageDirectoryEntrySecurity'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[4].VirtualAddress
    extracted_features['CheckSum'] = pe.OPTIONAL_HEADER.CheckSum
    extracted_features['SizeOfInitializedData'] = pe.OPTIONAL_HEADER.SizeOfInitializedData
    extracted_features['SizeOfImage'] = pe.OPTIONAL_HEADER.SizeOfImage
    extracted_features['MajorLinkerVersion'] = pe.OPTIONAL_HEADER.MajorLinkerVersion
    extracted_features['AddressOfEntryPoint'] = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    extracted_features['SectionMinEntropy'] = min(section.get_entropy() for section in pe.sections)
    extracted_features['DirectoryEntryImportSize'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].Size
    extracted_features['SectionMaxPhysical'] = max(section.PointerToRawData for section in pe.sections)
    extracted_features['SectionMinVirtualSize'] = min(section.Misc_VirtualSize for section in pe.sections)
    extracted_features['SectionMaxPointerData'] = max(section.SizeOfRawData for section in pe.sections)
    extracted_features['e_lfanew'] = pe.DOS_HEADER.e_lfanew
    extracted_features['DllCharacteristics'] = pe.OPTIONAL_HEADER.DllCharacteristics
    extracted_features['DirectoryEntryImport'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress
    extracted_features['ImageDirectoryEntryResource'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].VirtualAddress
    extracted_features['ImageDirectoryEntryImport'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress
    extracted_features['DirectoryEntryExport'] = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].VirtualAddress
    extracted_features['SizeOfCode'] = pe.OPTIONAL_HEADER.SizeOfCode
    extracted_features['ImageBase'] = pe.OPTIONAL_HEADER.ImageBase
    extracted_features['SizeOfStackReserve'] = pe.OPTIONAL_HEADER.SizeOfStackReserve

    # Extract values and store them in a vector
    features_vector = np.array(list(extracted_features.values()))
   
    return features_vector

# def extract_features(file_path):
#     pe = pefile.PE(file_path)
    
#     # Extract features
#     feature1 = pe.OPTIONAL_HEADER.DATA_DIRECTORY[4].VirtualAddress
#     feature2 = pe.OPTIONAL_HEADER.CheckSum
#     feature3 = pe.OPTIONAL_HEADER.SizeOfInitializedData
#     feature4 = pe.OPTIONAL_HEADER.SizeOfImage
#     feature5 = pe.OPTIONAL_HEADER.MajorLinkerVersion
#     feature6 = pe.OPTIONAL_HEADER.AddressOfEntryPoint
#     feature7 = min(section.get_entropy() for section in pe.sections)
#     feature8 = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].Size
#     feature9 = max(section.PointerToRawData for section in pe.sections)
#     feature10 = min(section.Misc_VirtualSize for section in pe.sections)
#     feature11 = max(section.SizeOfRawData for section in pe.sections)
#     feature12 = pe.DOS_HEADER.e_lfanew
#     feature13 = pe.OPTIONAL_HEADER.DllCharacteristics
#     feature14 = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress
#     feature15 = pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].VirtualAddress
#     feature16 = pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress
#     feature17 = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].VirtualAddress
#     feature18 = pe.OPTIONAL_HEADER.SizeOfCode
#     feature19 = pe.OPTIONAL_HEADER.ImageBase
#     feature20 = pe.OPTIONAL_HEADER.SizeOfStackReserve
    
#     return feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13, feature14, feature15, feature16, feature17, feature18, feature19, feature20


