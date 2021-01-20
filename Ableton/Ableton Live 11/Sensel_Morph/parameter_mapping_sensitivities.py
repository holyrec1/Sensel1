
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface import is_parameter_quantized
DEFAULT_SENSITIVITY_KEY = 'normal_sensitivity'
CONTINUOUS_MAPPING_SENSITIVITY = 1.0
QUANTIZED_MAPPING_SENSITIVITY = 0.2
PARAMETER_SENSITIVITIES = {'UltraAnalog': {'OSC1 Octave': {DEFAULT_SENSITIVITY_KEY: QUANTIZED_MAPPING_SENSITIVITY},
                  'OSC2 Octave': {DEFAULT_SENSITIVITY_KEY: QUANTIZED_MAPPING_SENSITIVITY},
                  'OSC1 Semi': {DEFAULT_SENSITIVITY_KEY: QUANTIZED_MAPPING_SENSITIVITY},
                  'OSC1 Detune': {DEFAULT_SENSITIVITY_KEY: 0.5},
                  'OSC2 Semi': {DEFAULT_SENSITIVITY_KEY: QUANTIZED_MAPPING_SENSITIVITY},
                  'OSC2 Detune': {DEFAULT_SENSITIVITY_KEY: 0.5}},
 'LoungeLizard': {'Noise Pitch': {DEFAULT_SENSITIVITY_KEY: 0.5},
                   'Damp Balance': {DEFAULT_SENSITIVITY_KEY: 0.5},
                   'P Amp < Key': {DEFAULT_SENSITIVITY_KEY: 0.5},
                   'Semitone': {DEFAULT_SENSITIVITY_KEY: 0.1},
                   'Voices': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'Collision': {'Res 1 Decay': {DEFAULT_SENSITIVITY_KEY: 0.5},
                'LFO 1 Sync Rate': {DEFAULT_SENSITIVITY_KEY: QUANTIZED_MAPPING_SENSITIVITY},
                'LFO 2 Sync Rate': {DEFAULT_SENSITIVITY_KEY: QUANTIZED_MAPPING_SENSITIVITY}},
 'InstrumentImpulse': {'1 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                        '2 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                        '3 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                        '4 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                        '5 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                        '6 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                        '7 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                        '8 Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5}},
 'OriginalSimpler': {'Mode': {DEFAULT_SENSITIVITY_KEY: 0.001},
                      'Playback': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Start': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'End': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Sensitivity': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'S Start': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'S Length': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'S Loop Length': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Transpose': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Detune': {DEFAULT_SENSITIVITY_KEY: 5.0},
                      'Gain': {DEFAULT_SENSITIVITY_KEY: 0.1},
                      'Env. Type': {DEFAULT_SENSITIVITY_KEY: 0.1},
                      'Filter Freq': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Filt < Vel': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Filt < Key': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Filt < LFO': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'LR < Key': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Vol < LFO': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Pan < RND': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'Pan < LFO': {DEFAULT_SENSITIVITY_KEY: 0.5},
                      'L Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Warp Mode': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Preserve': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Envelope': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Grain Size Tones': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Grain Size Texture': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Flux': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Formants': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'Envelope Complex Pro': {DEFAULT_SENSITIVITY_KEY: 0.2},
                      'L Retrig': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'Operator': {'A Coarse': {DEFAULT_SENSITIVITY_KEY: 0.25},
               'B Coarse': {DEFAULT_SENSITIVITY_KEY: 0.25},
               'C Coarse': {DEFAULT_SENSITIVITY_KEY: 0.25},
               'D Coarse': {DEFAULT_SENSITIVITY_KEY: 0.25},
               'LFO Sync': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'MultiSampler': {'O Coarse': {DEFAULT_SENSITIVITY_KEY: 0.25},
                   'L 1 Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.25},
                   'L 2 Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.25},
                   'L 3 Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'StringStudio': {'LFO SyncRate': {DEFAULT_SENSITIVITY_KEY: 0.2},
                   'Octave': {DEFAULT_SENSITIVITY_KEY: 0.2},
                   'Semitone': {DEFAULT_SENSITIVITY_KEY: 0.25},
                   'Fine Tune': {DEFAULT_SENSITIVITY_KEY: 0.5}},
 'MidiArpeggiator': {'Style': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Synced Rate': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Offset': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Transp. Steps': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Transp. Dist.': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Repeats': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Ret. Interval': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Groove': {DEFAULT_SENSITIVITY_KEY: 0.25},
                      'Retrigger Mode': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'MidiNoteLength': {'Synced Length': {DEFAULT_SENSITIVITY_KEY: 0.1}},
 'MidiPitcher': {'Pitch': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'MidiRandom': {'Choices': {DEFAULT_SENSITIVITY_KEY: 0.3},
                 'Scale': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'MidiScale': {'Base': {DEFAULT_SENSITIVITY_KEY: 0.2},
                'Transpose': {DEFAULT_SENSITIVITY_KEY: 0.25},
                'Range': {DEFAULT_SENSITIVITY_KEY: 0.1},
                'Lowest': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'Amp': {'Bass': {DEFAULT_SENSITIVITY_KEY: 0.5},
          'Middle': {DEFAULT_SENSITIVITY_KEY: 0.5},
          'Treble': {DEFAULT_SENSITIVITY_KEY: 0.5},
          'Presence': {DEFAULT_SENSITIVITY_KEY: 0.5},
          'Gain': {DEFAULT_SENSITIVITY_KEY: 0.5},
          'Volume': {DEFAULT_SENSITIVITY_KEY: 0.5},
          'Dry/Wet': {DEFAULT_SENSITIVITY_KEY: 0.5}},
 'AutoFilter': {'Frequency': {DEFAULT_SENSITIVITY_KEY: 1},
                 'Env. Modulation': {DEFAULT_SENSITIVITY_KEY: 0.5},
                 'LFO Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.1},
                 'LFO Phase': {DEFAULT_SENSITIVITY_KEY: 0.5},
                 'LFO Offset': {DEFAULT_SENSITIVITY_KEY: 0.5}},
 'AutoPan': {'Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.1}},
 'BeatRepeat': {'Grid': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Interval': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Offset': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Gate': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Pitch': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Variation': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Mix Type': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Grid': {DEFAULT_SENSITIVITY_KEY: 0.25},
                 'Variation Type': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'Corpus': {'LFO Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.1},
             'Transpose': {DEFAULT_SENSITIVITY_KEY: 0.25},
             'Fine': {DEFAULT_SENSITIVITY_KEY: 0.26}},
 'Echo': {'Mod Rate': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'Eq8': {'Band': {DEFAULT_SENSITIVITY_KEY: 0.5},
          '1 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4},
          '2 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4},
          '3 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4},
          '4 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4},
          '5 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4},
          '6 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4},
          '7 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4},
          '8 Frequency A': {DEFAULT_SENSITIVITY_KEY: 0.4}},
 'Flanger': {'Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.1}},
 'FrequencyShifter': {'Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'GrainDelay': {'Pitch': {DEFAULT_SENSITIVITY_KEY: 0.1}},
 'Phaser': {'LFO Sync Rate': {DEFAULT_SENSITIVITY_KEY: 0.1}},
 'Resonator': {'II Pitch': {DEFAULT_SENSITIVITY_KEY: 0.25},
                'III Pitch': {DEFAULT_SENSITIVITY_KEY: 0.25},
                'IV Pitch': {DEFAULT_SENSITIVITY_KEY: 0.25},
                'V Pitch': {DEFAULT_SENSITIVITY_KEY: 0.25}},
 'InstrumentVector': {'Osc 1 Pitch': {DEFAULT_SENSITIVITY_KEY: 5.0},
                       'Osc 2 Pitch': {DEFAULT_SENSITIVITY_KEY: 5.0},
                       'Osc 1 Category': {DEFAULT_SENSITIVITY_KEY: 0.5},
                       'Osc 2 Category': {DEFAULT_SENSITIVITY_KEY: 0.5},
                       'LFO 1 S. Rate': {DEFAULT_SENSITIVITY_KEY: 0.25},
                       'LFO 2 S. Rate': {DEFAULT_SENSITIVITY_KEY: 0.25},
                       'Unison Mode': {DEFAULT_SENSITIVITY_KEY: 0.5}}}

def sensitivity_mapping_for_parameter(parameter):
    is_quantized = is_parameter_quantized(parameter, parameter and parameter.canonical_parent)
    if is_quantized:
        return QUANTIZED_MAPPING_SENSITIVITY
    return CONTINUOUS_MAPPING_SENSITIVITY


def parameter_mapping_sensitivity(parameter, device_class = None):
    parameter_name = parameter.name if liveobj_valid(parameter) else ''
    try:
        return PARAMETER_SENSITIVITIES[device_class][parameter_name][DEFAULT_SENSITIVITY_KEY]
    except KeyError:
        return sensitivity_mapping_for_parameter(parameter)
